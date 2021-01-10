from django import forms
from .models import List

class PageUpdateForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('last_page',)
        labels = {
            'last_page': '',
        }