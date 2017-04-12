from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Place
#from .models import User




class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','company_name','email','first_name','last_name','password']

class PlaceForm(forms.ModelForm):
        class Meta:
            model = Place
            fields = ['username', 'company_name', 'license_id', 'geo_loc','profile_pic', 'info', 'address', 'tel_num','facebooklink', 'twitterlink', 'instagramlink', 'menu']

class ProfilePic(forms.ModelForm):

    class Meta:
        model = User
        fields = ['profile_pic']

class SettingsForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'company_name','profile_pic', 'info', 'tel_num','adress','facebooklink', 'twitterlink', 'instagramlink','password']

class MessageForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['message','password']

    #class UserForm(forms.ModelForm):

 #   class Meta:
   #     model = User
   #     fields = ['company_name','name_surname','license_id','geo_loc','username','email','password']



class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','password']