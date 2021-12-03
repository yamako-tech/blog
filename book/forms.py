from django import forms


class BookSearchForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200, required=True)