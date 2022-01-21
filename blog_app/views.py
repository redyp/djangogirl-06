from django.shortcuts import render, redirect, get_object_or_404

from blog_app.models import Post
from blog_app.form import PostForm

# Create your views here.
def home_views(request):
    if request.method == 'GET':
        posts = Post.objects.filter(published__isnull=False).order_by('-published')
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
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            post.save()
            return redirect('home')

def draft_post_views(request):
    drafts = Post.objects.filter(published__isnull=True)
    return render(
        request,
        'blog/draft.html',
        {
            'title': 'Draft Post',
            'drafts': drafts,
        }
    )

def save_as_draft_views(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

def publish_draft_post_views(request, pk):
    if request.method == 'GET':
        draft = get_object_or_404(Post, pk=pk)
        draft.publish()
        draft.save()
        return redirect('home')

def edit_post_views(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/form.html', {
            'title': f'Form Edit Post - {post.title.title()}',
            'form': form,
            'pk': pk,
        })
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
