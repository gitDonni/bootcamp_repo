from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/categories/')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    price_rent = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='images/product/')


    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'


class Features(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=120)
    features = models. CharField(max_length=120)

    def __str__(self):
        return f'{self.product} {self.title}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
