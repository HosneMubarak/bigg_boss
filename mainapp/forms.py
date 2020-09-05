from django import forms
from django.forms import ModelForm, Textarea
from .models import *


# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['program', 'publish_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        text = forms.CharField(max_length=200)
        fields = ['author', 'text']
        widgets = {
            'text': Textarea(attrs={'row': 1, 'cols': 1}),
        }
