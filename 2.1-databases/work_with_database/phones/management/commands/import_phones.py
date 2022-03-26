import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass
        # parser.add_argument('csv_file', nargs = '+', type = str)

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for item in phones:
            # phone = Phone()
            # phone.id = int(item.get('id')),
            # phone.name = item.get('name'),
            # phone.image = item.get('image'),
            # phone.price = item.get('price'),
            # phone.release_date = item.get('release_date'),
            # phone.lte_exists = item.get('lte_exists'),
            # phone.slug = phone.slug_name()

            phone = Phone(
                id = item.get('id'),
                name = item.get('name'),
                image = item.get('image'),
                price = item.get('price'),
                release_date = item.get('release_date'),
                lte_exists = item.get('lte_exists'),
                slug = slugify(item.get('name'))
            )


            try:
                phone.save()
                print(f'Телефон {phone} в базу внесён.')
            except:
                print(f'Что-то пошло не так. Телефон {phone} не был внесён')
