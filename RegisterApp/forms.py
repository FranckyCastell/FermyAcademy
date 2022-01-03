from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm (UserCreationForm):
    username = forms.CharField(label='Usuario', required=True)

    email = forms.EmailField(label='Correo electrónico', required=True)
    
    password1 = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)

    password2 = forms.CharField(label='Confirmar Contraseña', required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}
