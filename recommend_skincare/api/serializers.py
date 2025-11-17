import rest_framework
from rest_framework import serializers
from Products.models import Products
from Users.models import User
from UserActivity.models import UserActivity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model= UserActivity
        fields="__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields='__all__'


    