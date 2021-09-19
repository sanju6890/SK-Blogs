from django import forms
from django.forms import widgets
from .models import Comment, Post, Category, Comment

# choices = Category.objects.all().values_list('name', 'name')
# choice_list = []
# for item in choices:
#     choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Write a short and meaningful title for the blog...'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a tag for the blog...'}),
            # 'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'user_id','type':'hidden'}),
            'author': forms.TextInput(attrs={'class':'form-control','type':'hidden'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Write the blog here...'}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a snippet for the blog here...'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Write a short and meaningful title for the blog...'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Give a tag for the blog...'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Write the blog here...'}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a snippet for the blog here...'})
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Write a category name...'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Write a short and meaningful title for the blog...'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Write the blog here...'}),
        }