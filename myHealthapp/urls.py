from django.contrib import admin
from django.urls import path

from . import views
from .views import addPost

urlpatterns = [
    path('', views.home, name='homepage'),
    path('addPost', views.addPost, name='addPost'),
    path('allPosts', views.allPosts, name='allPosts'),
    path('deletePost/<p_id>', views.deletePost, name='deletePost'),
    path('editPost/<p_id>', views.editPost, name='editPost'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('contact', views.contact, name='contact'),
    path('therapieangebot', views.therapieangebot, name='therapieangebot'),


]
