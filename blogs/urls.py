from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Blogs Page
    path('blogs', views.blogs, name='blogs'),
    path('my_blogs', views.my_blogs, name='my_blogs'),
    path('blogs/<int:blog_id>', views.blog, name='blog'),

    # Blog edition or creation page
    path('new_blog', views.new_blog, name='new_blog'),
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),

    # Comments page
    path('new_comment/<int:blog_id>', views.new_comment, name='new_comment')
]
