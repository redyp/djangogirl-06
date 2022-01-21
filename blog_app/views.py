from django.shortcuts import render

# Create your views here.
def home_views(request):
    if request.method == 'GET':
        return render(request, 'index.html', {
            'title': 'Blog Post',
        })