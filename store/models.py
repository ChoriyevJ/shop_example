from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    objects = models.Manager()


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=10)

    objects = models.Manager()



