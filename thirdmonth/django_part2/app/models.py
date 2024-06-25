from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField(max_length=123)
    author = models.CharField(max_length=123, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

