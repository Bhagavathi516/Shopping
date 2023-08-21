from django import forms
from shopping.models import shoppingItemModel
from shopping.forms import shoppingItemForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.forms import formset_factory

class UserSignupEmailForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserSignupProfileForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")])
    place = forms.CharField(max_length=200)

UserSignupFormset = formset_factory(UserSignupProfileForm, extra=1)

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

ShoppingItemFormset = formset_factory(shoppingItemForm, extra=1)