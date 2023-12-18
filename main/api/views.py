from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer, AddBookSerializer


class AddBookAPI(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = AddBookSerializer(data=request.data)

        # if Book.objects.filter(title=serializer.data['title']).exists():
        if True:
            raise ValidationError("Такая книга уже есть в БД")
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})


class BookListAndDetailAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListAndDetailAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AddBookAPI(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
