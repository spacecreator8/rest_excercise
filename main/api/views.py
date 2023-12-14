from django.shortcuts import render
from rest_framework import generics

from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer

#TEST#TEST#TEST#TEST#TEST#TEST#TEST#TEST#TEST
class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#TEST#TEST#TEST#TEST#TEST#TEST#TEST#TEST#TEST
class AuthorListAPI(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


#TEST#TEST#TEST#TEST#TEST#TEST#TEST#TEST#TEST
class AuthorCreateAPI(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
