from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a comment...'
            }),
        }
        labels = {
            'comment': '',
        }
        help_texts = {
            'comment': 'Keep your comment respectful and relevant.',
        }