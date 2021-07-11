from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BooksList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    # path('db/', views.BooksUpdateList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
