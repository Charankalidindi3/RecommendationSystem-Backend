import rest_framework
from rest_framework import serializers
from Items.models import Items
from Users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Items
        fields='__all__'


    