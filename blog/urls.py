from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #from FBV
    path('blogs/', views.BlogListView.as_view(), name = 'blogs'), #from CBV
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name = 'blog-detail'),#also from CBV
    path('bloggers/', views.BloggerListView.as_view(), name = 'bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name = 'blogger-detail'),
    path('<int:pk>/create/', views.CommentCreate.as_view(), name='add_comment'),
    path('myread/', views.ReaderBlogListView.as_view(), name='my-read'),
]
