from django.contrib import admin
from django.urls import path, include

from api.views import BookListAPI, AuthorListAPI, AuthorCreateAPI

urlpatterns = [
    path('api/v1/booklist', BookListAPI.as_view()),
    path('api/v1/authorlist', AuthorListAPI.as_view()),
    path('api/v1/authorCreate', AuthorCreateAPI.as_view()),
]
