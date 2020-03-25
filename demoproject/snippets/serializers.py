from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id','email','username','password', 'first_name', 'last_name', 'phone']

class ProfilepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilepost
        #fields = ['id', 'title', 'author','email']
        fields='__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields='__all__'


"""
# For serializer instead of using modelserializer
class ProfilepostSerializer(serializers.Serializer):
     title = serializers.CharField(max_length=100)
     author = serializers.CharField(max_length=100)
     email = serializers.EmailField(max_length=100)
     date = serializers.DateTimeField()

     def create(self, validated_data):
        return Profilepost.objects.create(validated_data)

     def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author= validated_data.get('title', instance.author)
        instance.email = validated_data.get('title', instance.email)
        instance.date = validated_data.get('title', instance.date)
        instance.save()
        return instance"""
