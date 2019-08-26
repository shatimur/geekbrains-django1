from django.shortcuts import render

# Create your views here.


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'index.html', context=context)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
    context = {
        'title': 'Продукты',
        'links_menu': links_menu,
        # 'same_products': same_products,
    }
    return render(request, 'products.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'contact.html', context=context)
