from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
