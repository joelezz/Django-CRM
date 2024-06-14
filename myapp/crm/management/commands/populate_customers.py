from django.core.management.base import BaseCommand
from faker import Faker
from crm.models import Customer

class Command(BaseCommand):
    help = 'Populate the Customer model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        customers = []

        for _ in range(100):
            company = fake.company()
            position = fake.job()
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone = fake.phone_number()
            
            customer = Customer(
                company=company,
                position=position,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=fake.address(),
                city=fake.city(),
                postal_code=fake.postcode(),
                country=fake.country()
            )
            customers.append(customer)

        Customer.objects.bulk_create(customers)
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 100 dummy customers.'))
