from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone']


class ProfilepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilepost
        #fields = ['id', 'title', 'author','email']
        fields='__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields='__all__'

'''
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id','email','username','password', 'first_name', 'last_name', 'phone']
'''
