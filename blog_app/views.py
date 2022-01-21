from django.shortcuts import render, redirect

from blog_app.models import Post
from blog_app.form import PostForm

# Create your views here.
def home_views(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        return render(request, 'index.html', {
            'title': 'Blog Post',
            'posts': posts,
        })

def new_post_views(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blog/form.html', {
            'title': 'New Post Form',
            'form': form,
        })
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return redirect('home')
