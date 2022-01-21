from django.urls import path

from blog_app import views

urlpatterns = [
    path('', views.home_views, name='home'),
    path('blog/new', views.new_post_views, name='new_post'),
]
