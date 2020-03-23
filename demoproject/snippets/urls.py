from django.urls import path,include
from snippets import views

urlpatterns = [
     path('',include('djoser.urls')),
     path('',include('djoser.urls.authtoken')),
     path('restricted/',views.restricted),
     path('generic/news/<int:id>/', views.NewsGenericAPIView.as_view()),
     #path('profilepost/',views.profilepost_list),
     path('profilepost/',views.ProfilepostAPIView.as_view()),
     path('generic/profilepost/<int:id>/',views.GenericAPIView.as_view()),
     path('detail/<int:id>/',views.ProfilepostDetailAPIView.as_view())
     #path('detail/<int:pk>/',views.profilepost_detail)
]