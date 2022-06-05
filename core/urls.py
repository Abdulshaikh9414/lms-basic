"""
Created on 05-Jun-2022
@author: Abdulkadir
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/sign-up/', UserSignupAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view())
]