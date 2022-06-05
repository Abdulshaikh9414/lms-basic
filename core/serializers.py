"""
Created on 05-Jun-2022
@author: Abdulkadir
"""
from rest_framework import serializers
from .models import Book, User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'author', 'quantity', 'available']
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
