import csv
from django.core.management.base import BaseCommand
from route.models import FuelPrice

class Command(BaseCommand):
    help = 'Load fuel prices from CSV'

    def handle(self, *args, **kwargs):
        with open('fuel_prices.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            print(f"CSV Headers: {headers}")  # Print CSV headers for debugging

            for row in reader:
                print(row)  # Print each row to verify the keys
                FuelPrice.objects.create(
                    state=row['State'],
                    price_per_gallon=row['Retail Price']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded fuel prices'))
