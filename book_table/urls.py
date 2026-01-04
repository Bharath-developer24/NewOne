from django.urls import path
from .views import book_table_view
urlpatterns = [
    path('', book_table_view, name='book_table'),
]