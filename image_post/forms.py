from django import forms
from .models import ImagePost

class PostForm(forms.ModelForm):

    class Meta:
        model = ImagePost
        fields = ['title', 'description', 'image']