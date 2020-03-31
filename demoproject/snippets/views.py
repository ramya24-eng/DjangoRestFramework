# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Profilepost,News,User
from .serializers import NewsSerializer,UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from djoser.views import TokenDestroyView
from .pagination import PaginationView
from django.core.paginator import Paginator
from . import newsdb


#create your views here
#class based views
#@permission_classes([IsAuthenticated])
class UserCreateAPIView(APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@permission_classes([IsAuthenticated])
class UserCreateDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)

        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserCreateSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        instance = self.get_object(id)
        instance.first_name = request.data.get('first_name', instance.first_name)
        instance.last_name = request.data.get('last_name', instance.last_name)
        instance.phone = request.data.get('phone', instance.phone)
        instance.save()
        serializer = UserCreateSerializer(instance,data=request.data)
        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = self.get_object(id)
        user.delete()
        return Response(data="The respected user get deleted",status=status.HTTP_204_NO_CONTENT)

class NewsAPIView(APIView):
  #authentication_classes = [TokenAuthentication]
  #permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    queryset = News.objects.all()
    categories = self.request.query_params.get('category', '')
    print(categories)
    if categories is not None:
       queryset = queryset.filter(category=categories)
       paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    serializer = NewsSerializer(queryset, many=True)
    return Response({
            'count': paginator.count,
            'results': serializer.data
        })

