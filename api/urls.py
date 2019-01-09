from django.urls import path, include
from api import views


urlpatterns = [
    path('login/', views.loginview),
    path('processlogin/', views.processlogin),
    path('signup/', views.signup),
    path('register/', views.register),
    path('home/', views.home),
   
]