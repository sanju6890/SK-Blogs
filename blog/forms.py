from django import forms
from django.forms import widgets
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a short and meaningful title for the blog...'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a tag for the blog...'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'user_id','type':'hidden'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Start writing the blog here...'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a short and meaningful title for the blog...'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a tag for the blog...'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Start writing the blog here...'})
        }
