import csv
import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            Phone(id=int(phone['id']), name=phone['name'], price=float(phone['price']), image=phone['image'], release_date=datetime.datetime.strptime(phone['release_date'], '%Y-%m-%d'), lte_exists=bool(phone['lte_exists'])).save()
