import json
from django.shortcuts import render
import datetime
from .models import ProductCategory, Product


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

    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    context = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'same_products': same_products,
    }
    return render(request, 'products.html', context=context)


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
