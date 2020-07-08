from django.test import TestCase
from .models import Product, Category
# Create your tests here.


class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        category = Category.objects.create(
            name='Categoria Teste',
            description='Descrição Teste'
        )
        product = Product.objects.create(
            name='Teste Produto',
            description='Teste Description',
            price=10.5,
            category=category
        )

        self.assertEqual(str(product), 'Teste Produto')
