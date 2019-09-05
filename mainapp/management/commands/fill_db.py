from django.core.management.base import BaseCommand
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser

import json
import os

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'),
              'r',
              encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()

        for product in products:
            category_name = product['category']

            _category = ProductCategory.objects.get(name=category_name)

            product['category'] = _category

            new_product = Product(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('django',
                                                       'django@geekshop.local',
                                                       'geekbrains',
                                                       age=33)