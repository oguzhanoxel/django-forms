from django import forms
from .models import Book


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'desc', 'pages') # fields = '__all__'
        labels = {
            'title': 'Title',
            'author': 'Author',
            'desc': 'Description',
            'pages': 'Pages',
        }
