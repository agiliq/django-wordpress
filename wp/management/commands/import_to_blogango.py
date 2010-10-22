
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify

from wp.models import Post, Comment as WpComment
from blogango.models import BlogEntry, Comment


def get_auth_user(wp_author):
    try:
        auth_user = User.objects.get(username='wp_%s' % (wp_author.user_login))
    except User.DoesNotExist:
        auth_user = User.objects.create_user(username='wp_%s' % (wp_author.user_login),
                                             email = wp_author.user_email,
                                             first_name = wp_author.user_nicename)
    return auth_user

    
class Command(BaseCommand):
    help = 'Import blog posts from wordpress to blogango'
    def handle(self, *args, **kwargs):
        if 'blogango' not in settings.INSTALLED_APPS:
            raise CommandError('Add blogango to installed apps to import posts from wordpress')
        
        # get the offset id from blogango
        blog_entries = BlogEntry.objects.all().order_by('-id')
        offset = blog_entries.count() and blog_entries[0].id or 0
        wp_posts = Post.objects.filter(id__gt=offset, post_status='publish')
        
        for wp_post in wp_posts:
            # insert into BlogEntry
            blog_entry = BlogEntry.objects.create(id=wp_post.id,
                                                  title=wp_post.post_title,
                                                  slug=slugify(wp_post.post_title),
                                                  text=wp_post.post_content,
                                                  created_by=get_auth_user(wp_post.post_author))
            
            # add tags
            # wp_tags = 
            
            # add comments
            wp_comments = WpComment.objects.filter(comment_post_id=wp_post.id)
            for wp_comment in wp_comments:
                comment = Comment.objects.create(text=wp_comment,
                                                 comment_for=blog_entry,
                                                 user_name=wp_comment.comment_author,
                                                 user_url=wp_comment.comment_author_url)
    