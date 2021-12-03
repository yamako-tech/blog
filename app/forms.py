from django import forms
from .models import Category

class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category

    title = forms.CharField(max_length=30, label='title')
    category = forms.ChoiceField(label='category', widget=forms.Select, choices=list(category_choice.items()))
    content = forms.CharField(label='content', widget=forms.Textarea())
    image = forms.ImageField(label='postimage', required=False)

class BookSearchForm(forms.Form):
    title = forms.CharField(label='TITLE', max_length=200, required=True)