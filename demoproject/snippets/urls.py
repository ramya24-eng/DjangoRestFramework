from django.urls import path,include
from snippets import views

urlpatterns = [
     path('',include('djoser.urls')),
     path('',include('djoser.urls.authtoken')),
     path('register/',views.UserCreateAPIView.as_view()),
     path('registerdetail/<int:id>/',views.UserCreateDetailAPIView.as_view()),
     path('news/', views.NewsAPIView.as_view()),
]