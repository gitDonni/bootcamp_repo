from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='images/products/', null=True, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


class ProductImg(models.Model):
    image = models.ImageField(upload_to='image/products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
