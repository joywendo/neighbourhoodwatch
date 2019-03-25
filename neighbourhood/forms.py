from django import forms
from django.contrib.auth.models import User
from .models import Profile,Business,User,Neighbourhood,Comments



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio', 'neighbourhoodname','location']



class CommentForm(forms.ModelForm):
    class Meta:
        model =Comments
        exclude=['img','user']


class NhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude =['location']
