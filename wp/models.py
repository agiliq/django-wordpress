# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Commentmeta(models.Model):
    meta_id = models.IntegerField(primary_key=True)
    comment_id = models.IntegerField()
    meta_key = models.CharField(max_length=765, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = u'wp_commentmeta'

class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True, db_column='comment_ID') # Field name made lowercase.
    comment_post_id = models.IntegerField(db_column='comment_post_ID') # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=300)
    comment_author_url = models.CharField(max_length=600)
    comment_author_ip = models.CharField(max_length=300, db_column='comment_author_IP') # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=60)
    comment_agent = models.CharField(max_length=765)
    comment_type = models.CharField(max_length=60)
    comment_parent = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        db_table = u'wp_comments'

class Links(models.Model):
    link_id = models.IntegerField(primary_key=True)
    link_url = models.CharField(max_length=765)
    link_name = models.CharField(max_length=765)
    link_image = models.CharField(max_length=765)
    link_target = models.CharField(max_length=75)
    link_category = models.IntegerField()
    link_description = models.CharField(max_length=765)
    link_visible = models.CharField(max_length=60)
    link_owner = models.IntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=765)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=765)
    class Meta:
        db_table = u'wp_links'

class Options(models.Model):
    option_id = models.IntegerField(primary_key=True)
    blog_id = models.IntegerField()
    option_name = models.CharField(unique=True, max_length=192)
    option_value = models.TextField()
    autoload = models.CharField(max_length=60)
    class Meta:
        db_table = u'wp_options'

class Postmeta(models.Model):
    meta_id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    meta_key = models.CharField(max_length=765, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = u'wp_postmeta'

class Posts(models.Model):
    id = models.IntegerField(db_column='ID', primary_key = True) # Field name made lowercase.
    post_author = models.ForeignKey("wp.Users", db_column = "post_author")
    post_parent = models.ForeignKey("self", db_column="post_parent")
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_category = models.IntegerField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=60)
    comment_status = models.CharField(max_length=60)
    ping_status = models.CharField(max_length=60)
    post_password = models.CharField(max_length=60)
    post_name = models.CharField(max_length=600)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    guid = models.CharField(max_length=765)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=60)
    post_mime_type = models.CharField(max_length=300)
    comment_count = models.IntegerField()
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = u'wp_posts'
        
    def __unicode__(self):
        return self.post_title

class TermRelationships(models.Model):
    object_id = models.IntegerField(primary_key=True)
    term_taxonomy_id = models.IntegerField()
    term_order = models.IntegerField()
    class Meta:
        db_table = u'wp_term_relationships'

class TermTaxonomy(models.Model):
    term_taxonomy_id = models.IntegerField(primary_key=True)
    term_id = models.IntegerField(unique=True)
    taxonomy = models.CharField(max_length=96)
    description = models.TextField()
    parent = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        db_table = u'wp_term_taxonomy'

class Terms(models.Model):
    term_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=600)
    slug = models.CharField(unique=True, max_length=255)
    term_group = models.IntegerField()
    class Meta:
        db_table = u'wp_terms'

class Usermeta(models.Model):
    umeta_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    meta_key = models.CharField(max_length=765, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = u'wp_usermeta'

class Users(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user_login = models.CharField(max_length=180)
    user_pass = models.CharField(max_length=192)
    user_nicename = models.CharField(max_length=150)
    user_email = models.CharField(max_length=300)
    user_url = models.CharField(max_length=300)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=180)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=750)
    class Meta:
        db_table = u'wp_users'

class YarppKeywordCache(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    body = models.TextField()
    title = models.TextField()
    date = models.DateTimeField()
    class Meta:
        db_table = u'wp_yarpp_keyword_cache'

class YarppRelatedCache(models.Model):
    reference_id = models.IntegerField(primary_key=True, db_column='reference_ID') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    score = models.FloatField()
    date = models.DateTimeField()
    class Meta:
        db_table = u'wp_yarpp_related_cache'

