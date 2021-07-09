import requests
from django.db import migrations

from ..models import Book

# make a get request
r = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')

# get json content where the key is item
items = r.json()['items']

# support dictionary
details = {
    'book_id': None, 'title': None, 'authors': None, 'publishedDate': None,
    'categories': None, 'averageRating': None, 'ratingsCount': None,
    'imageLinks': None
}


# collect of the necessary data and preparation of the book object
def prepare_book(item):
    volume_info = item['volumeInfo']
    details['book_id'] = item['id']
    details.update({k: volume_info[k] for k in details if k in volume_info})

    if details['imageLinks'] is not None:
        details['imageLinks'] = volume_info.get('thumbnail')

    return Book(
        book_id=details['book_id'], title=details['title'],
        authors=details['authors'], published_date=details['publishedDate'],
        categories=details['categories'], average_rating=details['averageRating'],
        ratings_count=details['ratingsCount'], thumbnail=details['imageLinks']
    )


# reset values in the support dictionary to avoid assign incorrect data
# to the next books
def reset_values():
    return details.update({k: None for k in details})


# creation of book objects
def create_books(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    books = []

    for item in items:
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
