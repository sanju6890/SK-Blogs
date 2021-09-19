from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import widgets
from blog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'linkedin_url', 'twitter_url', 'instagram_url', 'facebook_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a short bio for your profile...'}),
            #'profile_pic': forms.TextInput(attrs={'class':'form-control'}),
            'website_url': forms.URLInput(attrs={'class':'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class':'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class':'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class':'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class':'form-control'}),
        }

class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'linkedin_url', 'twitter_url', 'instagram_url', 'facebook_url')
        widgets = {
            #'profile_pic': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a short bio for your profile...'}),
            'website_url': forms.URLInput(attrs={'class':'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class':'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class':'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class':'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']="form-control"
        self.fields['password1'].widget.attrs['class']="form-control"
        self.fields['password2'].widget.attrs['class']="form-control"

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')