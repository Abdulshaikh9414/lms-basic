"""
Created on 05-Jun-2022
@author: Abdulkadir
"""
from django.contrib import admin
from .models import Book, User

admin.site.register(User)
admin.site.register(Book)