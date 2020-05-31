from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView
from .models import Post

def post_list(request):
  object_list = Post.published.all()
  paginator = Paginator(object_list, 2) # This puts 3 posts on each page
  page = request.GET.get('page')
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an int then deliver the first page
    posts = paginator.page(1)
  except EmptyPage:
    # If page is out of range deliver last page of results
    posts = paginator.page(paginator.num_pages)
  return render(request,
                'blog/post/list.html',
                {'posts': posts})
# Returns a published post, given year, month, day and post
def post_detail(request, year, month, day, post):
  post = get_object_or_404(Post, slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
  return render(request,
                'blog/post/detail.html',
                {'post':post})

# Class based list view, this is analogous with def post_list
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'
# Create your views here.
