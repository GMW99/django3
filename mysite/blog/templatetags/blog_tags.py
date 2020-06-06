from django import template
from ..models import Post
register = template.Library()
# Returns  the  total published posts
@register.simple_tag
def total_posts():
    return Post.published.count()

# This speficies the template will be rendered the returned values using blog/post/latest_posts.html
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=2):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}