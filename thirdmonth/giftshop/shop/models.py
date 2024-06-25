from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=125)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class Banner(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'



class Application(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    message = models.TextField()


    def __str__(self):
        return f'Заявка от {self.name} - {self.email}'


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


