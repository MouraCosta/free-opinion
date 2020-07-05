from django import forms
from . import models


class NewBlogForm(forms.ModelForm):
    """A class to receive user input, for the creation of a blog."""
    class Meta:
        model = models.Blog
        fields = ['name', 'text']
        labels = {
            'name': 'Título:',
            'text': 'Sua opinião:'
        }
        widgets = {
            'name': forms.Textarea(attrs={'max_length': 50, 'cols': 10}),
            'text': forms.Textarea(attrs={'cols': 80})
        }


class NewCommentForm(forms.ModelForm):
    """A class to receive user input, for adding
    a new comment in a blog."""
    class Meta:
        model = models.Comment
        fields = ['text']
        labels = {'text': 'Texto'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
