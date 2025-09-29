from django import forms  # type:ignore
from App_Blog.models import Blog, Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,           # height of the box (3 lines)
                'cols': 50,          # width in characters
                'placeholder': 'Write your comment here...',
                'class': 'form-control',  # Bootstrap styling
            }),
        }
