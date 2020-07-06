from django.db import models
from products.models import Product

# Create your models here.


class Order(models.Model):
    name = models.CharField('Nome do CLiente', max_length=100)
    payment = models.CharField('Meio de Pagamento', max_length=50)
    products = models.ManyToManyField(Product)

    @property
    def total_amount(self):
        return sum([product.price for product in self.products.all()])

    def __str__(self):
        return f'{self.name} - {self.total_amount}'
