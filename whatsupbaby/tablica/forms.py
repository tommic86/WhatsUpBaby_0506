from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        labels = {
            'title': ('Tytuł'),
            'text': ('Treść')
        }
        
        #nadawanie nazw klasy
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'})
        }