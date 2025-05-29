from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class signup_form(UserCreationForm):
    first_name = forms.CharField(label='نام', max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'نام خود را وارد کنید'}))
    last_name = forms.CharField(label=' نام خانوادگی', max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'نام خانوادگی خود را وارد کنید'}))
    email = forms.EmailField(label='ایمیل',widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'ایمیل خود را وارد کنید'}))
    username = forms.CharField(label='نام کاربری' , widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'نام کاربری خود را وارد کنید'}))
    password1 = forms.CharField(label='رمز',widget=forms.PasswordInput(attrs={'class': 'form-control' }))
    password2 = forms.CharField(label='تکرار رمز', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name' , 'last_name' , 'email' , 'username' , 'password1' , 'password2' )