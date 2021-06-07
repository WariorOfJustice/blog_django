from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """
    Форма для регистрации джанго User-а с дополнительным обязательными полями.
    """
    email = forms.EmailField()
    first_name = forms.CharField(label='Имя пользователя')
    last_name = forms.CharField(label='Фамилия пользователя')
    username = forms.CharField(label='Псевдоним пользователя')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
