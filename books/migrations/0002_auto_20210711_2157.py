import requests
from django.db import migrations

from ..utils import prepare_book, reset_values

# make a get request
r = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')

# get json content where the key is item
items_hobbit = r.json()['items']


# creation of book objects
def create_books(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    books = []

    for item in items_hobbit:
        books.append(prepare_book(item))
        reset_values()
    Book.objects.bulk_create(books)


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_books),
    ]
