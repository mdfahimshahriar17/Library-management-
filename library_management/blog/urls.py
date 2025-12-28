from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/blog', views.create_blog, name='create_blog'),
    path('edit/blog/<int:pk>', views.edit_blog, name='edit_blog'),
    path('delete/blog/<int:pk>', views.delete_blog, name='delete_blog')
]