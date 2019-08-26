from django.shortcuts import render

# Create your views here.


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'index.html', context=context)


def products(request):
    context = {
        'title': 'Продукты'
    }
    return render(request, 'products.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'contact.html', context=context)
