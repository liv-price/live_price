from django.db import models


class ProductData(models.Model):
    product_name = models.CharField(max_length=100)
    permalink= models.CharField(max_length=12, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category= models.CharField(max_length=60)
    sub_category = models.CharField(max_length=60)
    model_number = models.CharField(max_length=60)
    identification_number = models.CharField(max_length=50, unique=True)
    site = models.CharField(max_length=50)
    update_date = models.DateTimeField('Last Updated')
    details= models.TextField('Product Details')

    def __str__(self):
        return self.product_name