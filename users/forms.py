from django import forms
from shopping.models import shoppingItemModel
from shopping.forms import shoppingItemForm
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.forms import formset_factory

class UserSignupEmailForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserSignupProfileForm(forms.ModelForm):
    # name = forms.CharField(max_length=200)
    # phone_number = forms.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")])
    # place = forms.CharField(max_length=200)
    # image = forms.ImageField(required=False, initial='default.jpg', upload_to='profile_pics')
    class Meta:
        model = UserProfile
        fields = ('name','phone_number', 'place', 'image')

UserSignupFormset = formset_factory(UserSignupProfileForm, max_num=1)

class UserUpdationForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class UserLoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.EmailField(widget=forms.EmailInput)
    # password = forms.CharField(strip=False, widget=forms.PasswordInput)

ShoppingItemFormset = formset_factory(shoppingItemForm, extra=1)