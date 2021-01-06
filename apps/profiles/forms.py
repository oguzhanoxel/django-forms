from django import forms
from .models import ReadingList

class PageUpdateForm(forms.ModelForm):

    class Meta:
        model = ReadingList
        fields = ('last_page',)
        labels = {
            'last_page': '',
        }