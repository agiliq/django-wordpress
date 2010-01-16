from django.contrib import admin
from wp.models import Post, PostMeta, WpUser, UserMeta, Term, TermTaxonomy, TermRelationship
from wp.models import Comment, CommentMeta, Link, Option, YarppKeywordCache, YarppRelatedCache


admin.site.register(Post)
admin.site.register(PostMeta)
admin.site.register(WpUser)
admin.site.register(UserMeta)
admin.site.register(Term)
admin.site.register(TermTaxonomy)
admin.site.register(TermRelationship)

admin.site.register(Comment)
admin.site.register(CommentMeta)
admin.site.register(Link)
admin.site.register(Option)
admin.site.register(YarppKeywordCache)
admin.site.register(YarppRelatedCache)
