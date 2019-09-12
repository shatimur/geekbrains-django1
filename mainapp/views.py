from django.shortcuts import render, get_object_or_404
import datetime
from .models import ProductCategory, Product
from basketapp.models import Basket
import random, os, json


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    products = Product.objects.all()
    title = 'главная'
    context = {
        'title': title,
        'products': products
    }
    return render(request, 'index.html', context=context)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)


    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': basket,
    }

    return render(request, 'products.html', content)

    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)
    #
    # if pk:
    #     if pk == '0':
    #         products = Product.objects.all().order_by('price')
    #         category = {'name': 'все'}
    #     else:
    #         category = get_object_or_404(ProductCategory, pk=pk)
    #         products = Product.objects.filter(category__pk=pk).order_by('price')
    #
    #     content = {
    #         'title': title,
    #         'links_menu': links_menu,
    #         'category': category,
    #         'products': products,
    #         'basket': basket,
    #     }
    #
    #     return render(request, 'mainapp/products_list.html', content)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    product = get_object_or_404(Product, pk=pk)

    content = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'basket': get_basket(request.user),
    }
    return render(request, 'product.html', content)


def contact(request):
    # locations = [
    #     {
    #         'city': 'Москва',
    #         'phone': '+7-888-888-8888',
    #         'email': 'info@geekshop-center.ru',
    #         'address': 'В пределах МКАД'
    #     },
    #     {
    #         'city': 'Санкт-Петербург',
    #         'phone': '+7-666-888-6666',
    #         'email': 'info@geekshop-nw.ru',
    #         'address': 'В пределах 100 км'
    #     },
    #     {
    #         'city': 'Казань',
    #         'phone': '+7-999-888-9999',
    #         'email': 'info@geekshop-tat.ru',
    #         'address': 'В пределах центра'
    #     }
    # ]
    # with open('geekshop/locations.json', 'w', encoding='utf-8') as f:
    #     json.dump(locations, f)

    with open('geekshop/locations.json', 'r', encoding='utf-8') as f:
        locations = json.load(f)

    context = {
        'title': 'Контакты',
        'locations': locations
    }


    return render(request, 'contact.html', context=context)
