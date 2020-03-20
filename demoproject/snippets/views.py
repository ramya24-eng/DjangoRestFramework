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
from .models import Profilepost
from .serializers import ProfilepostSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from newsapi import NewsApiClient

#create your views here
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request,*args,**kwargs):
    return Response(data="Only for logged in User", status=status.HTTP_200_OK)

#class based views
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


class ProfilepostDetailAPIView(APIView):
    def get_object(self,id):
        try:
            return Profilepost.objects.get(id=id)

        except Profilepost.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

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
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#Function based views
#Implementing with api_view
@api_view(['GET','POST'])
#@csrf_exempt
def profilepost_list(request):
    if request.method =='GET':
        profileposts = Profilepost.objects.all()
        serializer = ProfilepostSerializer(profileposts,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer =ProfilepostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#implementing without api_view
@csrf_exempt
def profilepost_detail(request, pk):
    try:
        profilepost = Profilepost.objects.get(pk=pk)

    except Profilepost.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfilepostSerializer(profilepost)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfilepostSerializer(profilepost,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        profilepost.delete()
        return HttpResponse(status=204)

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


def news(request):
    newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
    topheadlines = newsapi.get_everything(
        domains='bbc.co.uk,techcrunch.com',
        language='en',
        sort_by='relevancy')

    articles = topheadlines['articles']
    if articles.is_valid():
       articles.save()

    return JsonResponse(articles.data)
