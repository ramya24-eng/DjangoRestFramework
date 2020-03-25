from django.urls import path,include
from snippets import views

urlpatterns = [
     path('',include('djoser.urls')),
     path('',include('djoser.urls.authtoken')),
     path('restricted/',views.restricted),
     path('register/',views.UserCreateAPIView.as_view()),
     #path('registerdetail/',views.UserCreateDetailAPIView.as_view()),
     path('registerdetail/<int:id>/',views.UserCreateDetailAPIView.as_view()),
     path('profilepost/',views.ProfilepostAPIView.as_view()),
     path('profilepostdetail/<int:id>/',views.ProfilepostDetailAPIView.as_view()),
     path('generic/news/', views.NewsGenericAPIView.as_view()),
     path('generic/profilepost/<int:id>/', views.GenericAPIView.as_view()),
     # path('profilepost/',views.profilepost_list),
     #path('detail/<int:pk>/',views.profilepost_detail)
]