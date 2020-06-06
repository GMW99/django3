from django import template
from ..models import Post
register = template.Library()
# Returns  the  total published posts
@register.simple_tag
def total_posts():
    return Post.published.count()