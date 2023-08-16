from django import forms
from .models import shoppingItemModel

class shoppingItemForm(forms.ModelForm):
    class Meta:
        model = shoppingItemModel
        fields = "__all__"  