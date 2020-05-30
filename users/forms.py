from django.contrib.auth.forms import UserCreationForm
from django import forms
from users import models as models
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=27, help_text="Введите паррль для регирстрации")

    class Meta:
        model = models.Account
        fields = ("email", "username", "password1", "password2")

class AuthForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = models.Account
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["paswword"]

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid!")

        