from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Review


class LoginForm(AuthenticationForm):
    """this class for login form """

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'id': 'userName',
        'name': 'userName',
        'placeholder': 'Username',
        'type': 'text',
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'pwd',
        'name': 'password',
        'placeholder': 'Password',
        'class': 'form-control',
    }))


class RegisterForm(UserCreationForm):
    """this class for register form """

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'id': 'form3Example3',
        'placeholder': 'Username',
        'class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email address',
        'class': 'form-control',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'New password',
        'class': 'form-control',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ['username', 'email']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'review..',
            })
        }
