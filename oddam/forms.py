from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class NewUserForm(UserCreationForm):
    password1 = forms.CharField(label="Hasło", strip=False, widget=forms.PasswordInput(attrs={
        'placeholder': "Hasło"}), help_text=None)
    password2 = forms.CharField(label="Powtórz hasło", strip=False, widget=forms.PasswordInput(attrs={
        'placeholder': "Powtórz hasło"}), help_text=None)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")
        help_texts = {
            "username": None
        }
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': "Imie"}),
            "last_name": forms.TextInput(attrs={'placeholder': "Nazwisko"}),
            "username": forms.EmailInput(attrs={'placeholder': "Email"})
        }


class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
