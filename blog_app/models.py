from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def publish(self):
        self.published = timezone.now()
        self.save()
    
    def save_as_draft(self):
        self.published = None
        self.save()
    
    def text_as_list(self) -> list:
        return self.text.split('\n')