from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=120)


    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.title



class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)



    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

