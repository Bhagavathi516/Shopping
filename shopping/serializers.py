from django.contrib.auth.models import User, Group
from .models import shoppingItemModel
from rest_framework import serializers


class shoppingItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = shoppingItemModel
        fields = "__all__"  