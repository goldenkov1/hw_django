import os

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.truncate()
        Product.truncate()

        category_list = [
            {'pk': 1, 'name': 'CAPAROL',
             'description': 'немецкие краски и декоративные штукатурки для наружнего и внутреннего применения'},
            {'pk': 2, 'name': 'VGT', 'description': 'российские декоративные щтукатурки, лаки'},
            {'pk': 3, 'name': 'ALPINA', 'description': 'российские краски'},
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(**category))

        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        products_list = [
            {'product_name': 'capasilan',
             'description': 'глубокоматовая краска для потолков фирмы CAPAROL',
             'picture': "",
             'category': categories_for_create[0],
             'price': 110000
             },
            {'product_name': 'cera',
             'description': 'защитная восковая эмульсия для декоративных штукатурок фирмы VGT',
             'picture': "",
             'category': categories_for_create[1],
             'price': 18000},
            {'product_name': 'fassaden farbe',
             'description': 'краска для наружних работ фирмы  ALPINA',
             'picture': "",
             'category': categories_for_create[2],
             'price': 35000}
        ]

        for product in products_list:
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)
