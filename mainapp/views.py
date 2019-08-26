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
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop-center.ru',
            'address':'В пределах МКАД'
        },
        {
            'city': 'Санкт-Петербург',
            'phone': '+7-666-888-6666',
            'email': 'info@geekshop-nw.ru',
            'address': 'В пределах 100 км'
        },
        {
            'city': 'Казань',
            'phone': '+7-999-888-9999',
            'email': 'info@geekshop-tat.ru',
            'address': 'В пределах центра'
        }
    ]

    context = {
        'title': 'Контакты',
        'locations': locations
    }
    return render(request, 'contact.html', context=context)
