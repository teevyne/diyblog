from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from blog.models import Blog, Blogger, Theme, Language, BlogInstance
from . import views
from django.views import generic

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerDetailView(generic.DetailView):
    model = Blogger

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 1

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 2

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
        
    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ReaderBlogListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BlogInstance
    template_name ='blog/bloginstance_list_read_user.html'
