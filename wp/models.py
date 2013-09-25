from __future__ import unicode_literals

from django.db import models


class WpUser(models.Model):
    """This has been given a wp prefix, as contrib.user is so commonly
    imported name, and we do not want to namespace this everywhere."""

    id = models.BigIntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=64)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=60)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'Users'
        db_table = 'wp_users'

    def __unicode__(self):
        return self.user_nicename

class Link(models.Model):
    link_id = models.BigIntegerField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.ForeignKey(WpUser, db_column='link_owner')
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        verbose_name = u'Link'
        verbose_name_plural = u'Link'
        db_table = u'wp_links'

    def __unicode__(self):
        return self.link_name

class Option(models.Model):
    option_id = models.BigIntegerField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=64)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = u'Option'
        verbose_name_plural = u'Options'
        db_table = u'wp_options'
    
    def __unicode__(self):
        return self.option_name

class Post(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    post_author = models.ForeignKey(WpUser, db_column='post_author')
    post_parent = models.ForeignKey('self', db_column='post_parent')
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()

    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
        db_table = u'wp_posts'
   
    def __unicode__(self):
        return self.post_title or str(self.id)
    
    def get_absolute_url(self):
        return self.guid

class PostMeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    post = models.ForeignKey(Post)
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)
    
    class Meta:
        verbose_name = u'Post Meta'
        verbose_name_plural = u'Posts Meta'
        db_table = u'wp_postmeta'
    
    def __unicode__(self):
        return self.post.post_title or str(self.post.id) 

class Comment(models.Model):
    comment_id = models.BigIntegerField(db_column='comment_ID', primary_key=True) # Field name made lowercase.
    comment_post_id = models.ForeignKey(Post, db_column='comment_post_ID') # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100) # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()
    
    class Meta:
        verbose_name = u'Comment'
        verbose_name_plural = u'Comments'
        db_table = u'wp_comments'

    def __unicode__(self):
        return self.comment_content[:50]


class CommentMeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)

    class Meta:
        verbose_name = u'Comment Meta'
        verbose_name_plural = u'Comments Meta'
        db_table = u'wp_commentmeta'

    def __unicode__(self):
        return self.meta_key

class Term(models.Model):
    term_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)
    term_group = models.BigIntegerField()
    
    class Meta:
        verbose_name = u'Term'
        verbose_name_plural = u'Terms'
        db_table = u'wp_terms'

    def __unicode__(self):
        return self.name

class TermTaxonomy(models.Model):
    term_taxonomy_id = models.BigIntegerField(primary_key=True)
    term = models.ForeignKey(Term, unique=True)
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()
    
    class Meta:
        verbose_name = "Term Taxonomy"
        verbose_name_plural = "Term Taxonomies"
        db_table = u'wp_term_taxonomy'

    def __unicode__(self):
        return self.taxonomy


class TermRelationship(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    term_taxonomy = models.ForeignKey(TermTaxonomy)
    term_order = models.IntegerField()
    
    class Meta:
        verbose_name = u'Term Relationship'
        verbose_name_plural = u'Term Relationships'
        db_table = u'wp_term_relationships'

class UserMeta(models.Model):
    umeta_id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(WpUser)
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'User Meta'
        verbose_name_plural = 'Users Meta'
        db_table = u'wp_usermeta'

    def __unicode__(self):
        return self.user.user_nicename



