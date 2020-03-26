# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .models import Profilepost,News,User
from .serializers import ProfilepostSerializer,NewsSerializer,UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination


#create your views here
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request,*args,**kwargs):
    return Response(data="Only for logged in User", status=status.HTTP_200_OK)

#class based views
#@permission_classes([IsAuthenticated])
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

#@permission_classes([IsAuthenticated])
class UserCreateDetailAPIView(APIView):


    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    pagination_class = NewsViewPagination

    def get_queryset(self):
        queryset = News.objects.all()
        categories = self.request.query_params.get('category','')
        print (categories)
        if categories is not None:
            queryset =  queryset.filter(category = categories)
        return  queryset

