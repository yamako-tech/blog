from django.shortcuts import render
from django.views.generic import View
from .forms import BookSearchForm
import json
import requests

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&applicationId=1036371238913864295'

def get_api_data(params):
    api =requests.get(SEARCH_URL, params=params).text
    result = json.loads(api)
    items = result['Items']
    return items


class BookSearchView(View):
    def get(self, request, *args, **kwargs):
        form = BookSearchForm(request.POST or None)

        return render(request, 'book/booksearch.html', {
            'form': form,
        })
    def post(self, request, *args, **kwargs):
        form = BookSearchForm(request.POST or None)

        if form.is_valid():
            keyword = form.cleaned_data['title']
            params = {
                'title': keyword,
                'hits': 28,
            }
            items = get_api_data(params)
            book_data = []
            for i in items:
                item = i['Item']
                title = item['title']
                image = item['largeImageUrl']
                isbn = item['isbn']
                query = {
                    'title': title,
                    'image': image,
                    'isbn': isbn,
                }
                book_data.append(query)

            return render(request, 'book/booklist.html', {
                'book_data': book_data,
                'keyword': keyword,
            })

        return render(request, 'book/booksearch.html', {
            'form': form
        })

class BookDetailView(View):
    def get(self, request, *args, **kwargs):
        isbn = self.kwargs['isbn']
        params = {
            'isbn': isbn
        }

        items = get_api_data(params)
        items = items[0]
        item = items['Item']
        title = item['title']
        image = item['largeImageUrl']
        author = item['author']
        itemPrice = item['itemPrice']
        salesDate = item['salesDate']
        publisherName = item['publisherName']
        size = item['size']
        isbn = item['isbn']
        itemCaption = item['itemCaption']
        itemUrl = item['itemUrl']
        reviewAverage = item['reviewAverage']
        reviewCount = item['reviewCount']

        book_data = {
            'title': title,
            'image': image,
            'author': author,
            'itemPrice': itemPrice,
            'salesDate': salesDate,
            'publisherName': publisherName,
            'size': size,
            'isbn': isbn,
            'itemCaption': itemCaption,
            'itemUrl': itemUrl,
            'reviewAverage': reviewAverage,
            'reviewCount': reviewCount,
            'average': float(reviewAverage) * 20
        }

        return render(request, 'book/bookdetail.html', {
            'book_data': book_data
        })




