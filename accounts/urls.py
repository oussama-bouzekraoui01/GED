from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('index/', views.home),
    path('login/',views.loginPage),
    path('register/',views.register),
    path('update/',views.update),
    path('password-change/',views.passwordChange),
    path('profile/',views.profile)
]