from django import forms
from .models import Book, Category

class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'category', 'desc', 'pages') # fields = '__all__'
        labels = {
            'title': 'Title',
            'author': 'Author',
            'category': 'Select Category',
            'desc': 'Description',
            'pages': 'Pages',
        }

class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title',) # fields = '__all__'
        labels = {
            'title': 'Add Category',
        }

class CategoryDeleteForm(forms.Form):
    category = forms.ModelChoiceField(queryset= Category.objects.all())
