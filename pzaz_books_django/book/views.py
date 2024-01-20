from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer


class LatestBookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()[0:4]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetail(APIView):
    def get_object(self, category_slug, book_slug):
        try:
            return Book.objects.filter(category__slug=category_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, book_slug, format=None):
        book = self.get_object(category_slug, book_slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class Books(APIView):
    def get_category(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_data = request.data
        category_slug = request_data["category_slug"]
        category = self.get_category(category_slug)
        Book.objects.create(
            category_id=category.id,
            name=request_data["name"],
            slug=request_data["slug"],
            price=request_data["price"],
            description=request_data["description"],
            # image=request_data["image"],
        )
        response_data = {"response": "Book created successfully"}
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        request_data = request.data
        category_slug = request_data["category_slug"]
        category = self.get_category(category_slug)

        book = Book.objects.get(id=id)

        if book is None:
            response_data = {"response": "Book does not exists"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        book.category_id = category.id if category else book.category_id
        book.name = request_data.get("name", book.name)
        book.slug = request_data.get("slug", book.slug)
        book.price = request_data.get("price", book.price)
        book.description = request_data.get("description", book.description)
        book.save()
        response_data = {"response": "Book updated successfully"}
        return Response(response_data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        id = request.data.get('id')
        book = Book.objects.get(id=id)
        if book is None:
            response_data = {"response": "Book does not exists"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        response_data = {"response": "Book deleted successfully"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def search(request):
    query = request.data.get("query", "")
    if query:
        books = Book.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({"books": []})
