from os import name
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.user_register,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
