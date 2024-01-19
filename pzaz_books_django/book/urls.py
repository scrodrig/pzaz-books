from django.urls import path, include

from book import views

urlpatterns = [
  path("latest-books/", views.LatestBookList.as_view()),
  path("books/<slug:category_slug>/<slug:book_slug>", views.BookDetail.as_view()),
]