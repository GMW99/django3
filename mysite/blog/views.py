from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm

"""
This view works as follows:

"""
def post_share(request,post_id):
  # Retrive post by id and make sure its published
  post = get_object_or_404(Post,id=post_id, status='published')
  if request.method == 'POST':
    # Create form with inputs
    form = EmailPostForm(request.POST)
    if form.is_valid():
      # Form fields passed validation check
      cd = form.cleaned_data
      # create dictionary with  clean data
      # ... send data
  else:
    # When loaded (GET request) create a new form instance, will be used for template
    form = EmailPostForm()
  return render(request,'blog/post/share.html', {'post':post,
                                                 'form': form})


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
