from django.shortcuts import render, redirect
# from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import Product
from .forms import ProductModelForm

# Create your views here.


# @cache_page(settings.CACHE_TTL)
def list_products(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'products/list.html', context=context)


def create_product(request):

    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductModelForm()
            return redirect('products:list')
    else:
        form = ProductModelForm()

    context = {'form': form}
    return render(request, 'products/create.html', context=context)


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products:list')


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductModelForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductModelForm(instance=product)

    context = {
        'form': form
    }

    return render(request, 'products/update.html', context=context)
