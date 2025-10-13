from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username','password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите электронную почту'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите город'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'city','password1', 'password2')


class UserProfileFrom(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, 'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True, 'class':'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, 'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','city')