from django.shortcuts import render
from .models import Category, Product, Image


def categories_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories,
    }
    return render(request, 'products/categories_list.html', ctx)


def products_list(request, id):
    products = Product.objects.filter(categories=id)
    category = Category.objects.get(id=id)
    ctx = {
        'products': products,
    }
    return render(request, 'products/products_list.html', ctx)


def product_description(request, id):
    product = Product.objects.get(id=id)
    images = Image.objects.filter(product=id)
    ctx = {
        'product': product,
        'images': images,
    }
    return render(request, 'products/product_description.html', ctx)
