from django.urls import path
from book import views

urlpatterns = [
    path('booksearch/', views.BookSearchView.as_view(), name='book_booksearch'),
    # path('booklist/', views.BookListView.as_view(), name='book_booklist'),
    path('bookdetail/<str:isbn>', views.BookDetailView.as_view(), name='book_bookdetail'),
]