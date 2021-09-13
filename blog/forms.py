from django import forms
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a short and meaningful title for the blog...'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a tag for the blog...'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Start writing the blog here...'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a short and meaningful title for the blog...'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a tag for the blog...'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Start writing the blog here...'})
        }
