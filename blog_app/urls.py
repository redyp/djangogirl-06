from django.urls import path

from blog_app import views

urlpatterns = [
    path('', views.home_views, name='home'),
    path('blog/new', views.new_post_views, name='new_post'),
    path('blog/draft', views.draft_post_views,name='draft_post'),
    path('blog/new/draft', views.save_as_draft_views,name='save_as_draft'),
    path('blog/draft/<int:pk>', views.publish_draft_post_views,name='publish_draft_post'),
    path('blog/edit/<int:pk>', views.edit_post_views,name='edit_post'),
    path('blog/delete/<int:pk>', views.delete_post,name='delete_post')
]
