from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class LatestBookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()[0:4]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
