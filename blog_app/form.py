from django.forms import ModelForm

from blog_app.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'text',
        )