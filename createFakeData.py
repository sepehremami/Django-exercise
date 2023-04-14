import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_store.settings")
from random import randint
import django
django.setup()

from faker import factory, Faker
from users.models import * 
from library.models import Book
from basket.models import Basket
from warehouse.models import Warehouse
from model_bakery.recipe import Recipe, foreign_key

fake = Faker()

for k in range(10):
    author=Recipe(Athur, 
                  name=fake.name(), 
                  address=fake.address(), 
                  url=fake.url(),)
    
    customer=Recipe(Customer, 
                name= fake.name(),
                address= fake.address(), 
                phone=fake.phone_number(), 
                email=fake.email(),)
    
    publisher=Recipe(Publisher, 
                    address=fake.address(),
                    name=fake.name(),
                    phone=fake.phone_number(),
                    url=fake.url(),)
    
    # warehouse=Recipe(Warehouse, 
    #                 code=fake.unique.random_int(), 
    #                 phone=fake.phone_number(),
    #                 address=fake.address(),)
    
    book=Recipe(Book, 
                isbn=fake.unique.isbn10(),
                title=fake.name(),
                year= fake.past_date(),
                price=randint(1, 1000),
                author=foreign_key(author),
                publisher=foreign_key(publisher),
                # warehouse=foreign_key(warehouse)
                )
    
    basket=Recipe(Basket,
                   customer=foreign_key(customer),
                   book=foreign_key(book)
                )
    book.make()
    basket.make()
    publisher.make()
    customer.make()
    author.make()
