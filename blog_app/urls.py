from django.urls import path

from blog_app import views

urlpatterns = [
    path('', views.home_views, name='home'),
    path('blog/new', views.new_post_views, name='new_post'),
    path('blog/draft', views.draft_post_views,name='draft_post'),
    path('blog/new/draft', views.save_as_draft_views,name='save_as_draft'),
    path('blog/draft/<int:pk>', views.publish_draft_post_views,name='publish_draft_post'),
]
