from django.shortcuts import render
from .models import Product


def main(request):
    product_list = Product.objects.all()

    return render(request, 'mainapp/index.html', context={'user': {'name': 'Pavel', 'surname': 'Ilinykh'}, 'products': product_list})


def products(request, pk=None):
    return render(request, 'mainapp/products.html')


def contacts(request, pk=None):
    return render(request, 'mainapp/contacts.html')