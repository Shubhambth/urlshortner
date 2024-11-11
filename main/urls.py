from os import name
from django.urls import path
from .views import home , redirect_view, final_redirect_view 

urlpatterns = [
    path('home/', home, name='home'),
    path('<str:short_path>/', redirect_view, name='redirect_view'),
    path('<str:short_path>/go/', final_redirect_view, name='final_redirect'),
    
]