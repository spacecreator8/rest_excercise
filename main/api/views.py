from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
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
        serializer.is_valid(raise_exception=True)

        #проверка на наличие одноименной книги
        if Book.objects.filter(title=serializer.validated_data['title']).exists():
            queryset = Book.objects.filter(title=serializer.validated_data['title'])
            raise_ex_flag = True

            #Здесь делается проверка для художественных книг
            if serializer.validated_data['category'] == 0:
                for i in queryset:
                    if serializer.validated_data['category'] == 0 and i.publisher != serializer.validated_data['publisher']:
                        raise_ex_flag = False
                    else:
                        raise_ex_flag = True
                        break
            # Здесь делается проверка для научных книг
            if serializer.validated_data['category'] == 1:
                for i in queryset:
                    if serializer.validated_data['category'] == 1 and i.yearOfRel != serializer.validated_data['yearOfRel']:
                        raise_ex_flag = False
                    else:
                        raise_ex_flag = True
                        break

            if raise_ex_flag:
                raise ValidationError('В БД уже есть книга с таким названием.')
            else:
                serializer.save()
                return Response({'post': "успешно добавлена запись"})

        #если нет одноименной книги
        serializer.save()
        return Response({'post': "запись успешно добавлена"})


class BookListAndDetailAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'genre']


class AuthorListAndDetailAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
