from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from .models import posts, superuser


class postForm(ModelForm):
    class Meta:
        model = posts
        fields = ["title", "body", "url", "audio_link", "audio"]
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            'url': forms.TextInput(attrs= {'class': 'form-control'}),
            'audio_link': forms.TextInput(attrs= {'class': 'form-control'}),


        }


class profileForm(ModelForm):
    class Meta:
        model = superuser
        fields = ["Firstname", "Lastname", "bio", "profile_img"]
        widgets = {
            'names': forms.TextInput(attrs= {'class': 'form-control'}),
            'bio': forms.Textarea(attrs= {'class': 'form-control'}),
            #'profile_img': forms.Media(attrs= {'class': 'form-control'})
        }
    

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    need = forms.CharField()
    message = forms.TextInput()