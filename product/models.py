from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "categories"

class Product(models.Model):
    name       = models.CharField(max_length=50)
    price      = models.CharField(max_length=100)
    category   = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"
