import csv

from django.apps import apps
from django.core.management.base import BaseCommand
from PodzialPolski.models import Woj, Pow, Gmi, Miasto


class Command(BaseCommand):
    def handle(self, *args, **options):
        filename = 'SIMC.csv'
        with open(filename, 'r', encoding='utf-8') as TERC:
            reader = csv.DictReader(TERC, delimiter=';', fieldnames=[
                'WOJ',
                'POW',
                'GMI',
                'RODZ_GMI',
                'RM',
                'MZ',
                'NAZWA',
                'SYM',
                'SYMPOD',
                'STAN_NA',
            ])
            next(reader)
            for row in reader:
                try:
                    gmi = Gmi.objects.get(symbol=row['GMI'], powiat__symbol=row['POW'], powiat__woj__symbol=row['WOJ'])
                    name = row['NAZWA']

                    # Sprawdź, czy miasto już istnieje w bazie danych, jeśli tak, pomijaj
                    if not Miasto.objects.filter(gmina=gmi, name=name).exists():
                        Miasto.objects.create(gmina=gmi, name=name)
                        print(name, '++')
                    else:
                        print(name, 'pominięte')
                except Gmi.DoesNotExist:
                    print(f"BRAK - {row['NAZWA']}")

            # USUWANIE MIAST ##
            # for row in reader:
            #     try:
            #         miasto = Miasto.objects.filter(gmina=apps.get_model('PodzialPolski.Gmi').objects.get(symbol=row['GMI'], powiat__symbol=row['POW'], powiat__woj__symbol=row['WOJ']), name=row['NAZWA'])
            #         miasto.delete()
            #         print(row['NAZWA'], 'usunieto')
            #     except Gmi.DoesNotExist:
            #         print('ni ma')




