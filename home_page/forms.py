from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser
import re


class UserRegisterForm(UserCreationForm):
    
    error_messages = {
        'invalid email':_('Invalid email.'),
        "password_mismatch": _("The two password fields didn’t match."),
        'username_exists':_('Username already exists.')
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id':'password',
                'class':'',
                'type':'password',
                "autocomplete": "new-password",
            }),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id':'confirm_password',
                'class':'',
                'type':'password',
                "autocomplete": "new-password",
            }),
    )
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
        )
    
    # Validaciones
    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        regex = re.compile(r"([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,4}){1,2}")
        if not re.fullmatch(regex, email):
            raise ValidationError(
                self.error_messages['invalid email'],
                code='invalid_data',
            )
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        exists = CustomUser.objects.filter(username=username).exists()
        print(exists)
        if exists:
            raise ValidationError(
                self.error_messages['username_exists'],
                code='username_exists',
            )
        return username
        

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
        )
        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'id':'email',
                    'class':'',
                    'type':'email',
                    'minlength':1,
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'id':'password',
                    'class':'',
                    'type':'password',
                    'minlength':8,
                }
            ),
        }


