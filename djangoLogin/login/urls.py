from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('login/',login_view,name="login_view"),
    path('loginout/',logout_view,name="logout_view"),
]