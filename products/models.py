from django.db import models

# Create your models here.


class ProductManager(models.Manager):
    def with_text(self, text: str) -> models.QuerySet:
        """
            Pesquisa os produtos cujo nome contenha "text".

            :return: **QuerySet** com o filtro aplicado.
        """
        queryset = self.get_queryset().filter(name__contains=text)
        return queryset

    def expensive_products(self) -> models.QuerySet:
        """
            Realiza o filtro dos produtos cujo preço seja maior do que 500 reais.

            :return: **QuerySet** com o filtro aplicado.
        """
        return self.get_queryset().filter(price__gte=500)

    def cheap_toys(self) -> models.QuerySet:
        """
            Retorna a lista com os brinquedos mais baratos.

            :return: **QuerySet** com o filtro aplicado.
        """
        return self.get_queryset().filter(category__name='Brinquedos', price__lte=500)

    def test_doc(self):
        self.with_text()
        self.expensive_products()
        self.cheap_toys()


class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return f'{self.name} - {self.products.count()}'

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """
        Model contendo todos os campos necessários para
        cadastrar produtos no eComm
    """
    objects = ProductManager()

    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name='products')

    def __str__(self):
        return self.name
