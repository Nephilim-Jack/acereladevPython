from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.


class CategoryModelAdmin(admin.ModelAdmin):
    def products(self, obj):
        href = reverse('admin:products_product_changelist') + \
            f'?category={obj.pk}'
        return format_html(f'<a href="{href}">{obj.products.count()}</a>')

    products.short_description = 'Produtos da Categoria'

    list_display = ('name', 'description', 'products')


class ProductModelAdmin(admin.ModelAdmin):
    def formated_price(self, obj):
        return f'R${obj.price}'

    def link_category(self, obj):
        href = reverse('admin:products_category_change',
                       args=(obj.category.pk, ))
        return format_html(f'<a href={href}>{obj.category.name}</a>')

    formated_price.short_description = 'Preço'
    link_category.short_description = 'Categoria'
    list_display = ('name', 'formated_price', 'description', 'link_category')


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
