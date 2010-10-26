
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify

from wp.models import Post, Comment as WpComment, TermTaxonomy, TermRelationship, Term
from blogango.models import BlogEntry, Comment, Reaction

def get_auth_user(wp_author):
    try:
        auth_user = User.objects.get(username='wp_%s' % (wp_author.user_login))
    except User.DoesNotExist:
        auth_user = User.objects.create_user(username='wp_%s' % (wp_author.user_login),
                                             email = wp_author.user_email)
        auth_user.first_name = wp_author.user_nicename
        auth_user.save()
    return auth_user

COMMENT_AGENTS = ['btc_reddit', 'btc_yc', 'btc_twitter', 'btc_friendfeed', 'btc_blog']    
class Command(BaseCommand):
    help = 'Import blog posts from wordpress to blogango'
    def handle(self, *args, **kwargs):
        if 'blogango' not in settings.INSTALLED_APPS:
            raise CommandError('Add blogango to installed apps to import posts from wordpress')
        
        # get the offset id from blogango
        blog_entries = BlogEntry.objects.all().order_by('-id')
        offset = blog_entries.count() and blog_entries[0].id or 0
        wp_posts = Post.objects.filter(id__gt=offset, post_status='publish', post_type='post')
        
        for wp_post in wp_posts:
            # insert into BlogEntry
            print wp_post.post_date

            blog_entry = BlogEntry.objects.create(id=wp_post.id,
                                                  title=wp_post.post_title,
                                                  slug=slugify(wp_post.post_title),
                                                  text=wp_post.post_content,
                                                  created_by=get_auth_user(wp_post.post_author))
            blog_entry.created_on = wp_post.post_date
            blog_entry.save()
            
            tables = ['wp_term_taxonomy', 'wp_term_relationships']
            where = ['wp_term_relationships.object_id = %s', 
                     'wp_term_taxonomy.term_taxonomy_id = wp_term_relationships.term_taxonomy_id', 
                     'wp_term_taxonomy.term_id = wp_terms.term_id', 
                     'wp_term_taxonomy.taxonomy = %s']
                
            # get categories
            categories = Term.objects.extra(tables=tables, where=where, params=[wp_post.id, 'category'])
            for category in categories:blog_entry.tags.add(category.name)
            
            # get tags
            # tags = Term.objects.extra(tables=tables, where=where, params=[wp_post.id, 'post_tag'])
            # for tag in tags:blog_entry.tags.add(tag.name)
            
            # add comments
            wp_comments = WpComment.objects.filter(comment_post_id=wp_post.id, comment_approved=1)
            for wp_comment in wp_comments:
                if wp_comment.comment_type == 'pingback':continue
                if wp_comment.comment_agent in COMMENT_AGENTS:
                    comment = Reaction.objects.create(text=wp_comment.comment_content,
                                                       comment_for=blog_entry,
                                                       user_name=wp_comment.comment_author,
                                                       user_url=wp_comment.comment_author_url,
                                                       source=wp_comment.comment_agent.lstrip('btc_'))
                else:
                    comment = Comment.objects.create(text=wp_comment.comment_content,
                                                     comment_for=blog_entry,
                                                     user_name=wp_comment.comment_author,
                                                     user_url=wp_comment.comment_author_url,
                                                     email_id=wp_comment.comment_author_email)
                comment.created_on = wp_comment.comment_date
                comment.is_public = True
                comment.save()
   