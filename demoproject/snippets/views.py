# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Profilepost,News,User
from .serializers import ProfilepostSerializer,NewsSerializer,UserCreateSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from newsapi import NewsApiClient
from rest_framework.pagination import LimitOffsetPagination
from snippets import newsdb

#create your views here
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request,*args,**kwargs):
    return Response(data="Only for logged in User", status=status.HTTP_200_OK)




#class based views
@permission_classes([IsAuthenticated])
class UserCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class UserCreateDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)

        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserCreateSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = self.get_object(id)
        serializer = UserCreateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = self.get_object(id)
        user.delete()
        return Response(data="The respected user get deleted",status=status.HTTP_204_NO_CONTENT)


class NewsViewPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5


class NewsGenericAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsViewPagination

    def get_queryset(self):
        queryset = News.objects.all()
        categories = self.request.query_params.get('category','')
        print (categories)
        if categories is not None:
            queryset =  queryset.filter(category = categories)
        return  queryset

'''
@permission_classes([IsAuthenticated])
class ProfilepostAPIView(APIView):
    def get(self,request):
        profileposts = Profilepost.objects.all()
        serializer = ProfilepostSerializer(profileposts, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProfilepostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class ProfilepostDetailAPIView(APIView):
    def get_object(self,id):
        try:
            return Profilepost.objects.get(id=id)

        except Profilepost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
         profilepost = self.get_object(id)
         serializer = ProfilepostSerializer(profilepost)
         return Response(serializer.data)

    def put(self,request,id):
        profilepost = self.get_object(id)
        serializer = ProfilepostSerializer(profilepost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        profilepost = self.get_object(id)
        profilepost.delete()
        return Response(data="The respected user get deleted",status=status.HTTP_204_NO_CONTENT)


#generic_views
class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ProfilepostSerializer
    queryset = Profilepost.objects.all()
    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication,BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request,id)

    def delete(self, request):
        return self.destroy(request,id)
'''
