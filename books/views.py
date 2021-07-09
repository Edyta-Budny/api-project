from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BooksList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        author = self.request.query_params.get('author')
        published_date = self.request.query_params.get('published_date')
        sort_type = self.request.query_params.get('sort')
        if author is not None:
            author = books.filter(authors='[' + author + ']')
            serializer = BookSerializer(author, many=True)
            return Response(serializer.data)
        elif published_date is not None:
            published_date = books.filter(published_date=published_date)
            serializer = BookSerializer(published_date, many=True)
            return Response(serializer.data)
        elif sort_type is not None and sort_type.startswith('-'):
            books = books.order_by('published_date')
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)


class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
