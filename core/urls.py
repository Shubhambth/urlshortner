
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urls/' ,include('main.urls')),
    path('',include('authuser.urls')),
]
