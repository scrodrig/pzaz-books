from django.urls import path, include

from book import views

urlpatterns = [
  path("latest-books/", views.LatestBookList.as_view()),
  path("all-books/", views.Books.as_view()),
  path("books/create/", views.Books.as_view()),
  path("books/update/<int:id>", views.Books.as_view()),
  path("books/delete/", views.Books.as_view()),
  path("books/search/", views.search),
  path("books/<slug:category_slug>/<slug:book_slug>/", views.BookDetail.as_view()),
  path("books/<slug:category_slug>/", views.CategoryDetail.as_view()),
]