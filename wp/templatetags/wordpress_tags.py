from django import template
from wp.models import Post, Comment


register = template.Library()


@register.inclusion_tag("wp/recent_comments.html")
def show_comments(num_comments):
    return {"comments":Comment.objects.order_by("-comment_date")[:num_comments]}


@register.inclusion_tag("wp/recent_posts.html")
def show_posts(num_comments):
    return {"posts": Post.objects.filter(post_type="post", post_status="publish").order_by("-post_date")[:num_comments]}

@register.tag
def populate_comments(parser, token):
    "Use: {% populate_comments 5 as recent_comments %}"
    try:
        tag_name, num_comments, as_name, name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("populate_comments requires three argument")
    return CommentsNode(num_comments, name)

class CommentsNode(template.Node):
    def __init__(self, num_comments, name):
        self.num_comments = num_comments
        self.name = name
    
    def render(self, context):
        ""
        context[self.name] = Comment.objects.order_by("-comment_date")[:self.num_comments]
        return ""
            
@register.tag
def populate_posts(parser, token):
    "Use: {% populate_posts 5 as recent_comments %}"
    try:
        tag_name, num_posts, as_name, name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("populate_posts requires three argument")
    return PostsNode(num_posts, name)

class PostsNode(template.Node):
    def __init__(self, num_posts, name):
        self.num_posts = num_posts
        self.name = name
    
    def render(self, context):
        ""
        context[self.name] = Post.objects.filter(post_type="post", post_status="publish").order_by("-post_date")[:self.num_posts]
        return ""
    

    

