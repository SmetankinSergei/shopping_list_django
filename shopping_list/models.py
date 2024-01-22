from django.db import models
from django.db.models import PROTECT

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('create_at',)


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name='name')
    details = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=PROTECT, related_name='products')
    img = models.ImageField(upload_to='product_img/', **NULLABLE)
    price = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('change_at',)
