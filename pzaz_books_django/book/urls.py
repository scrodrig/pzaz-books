from django.urls import path, include

from book import views

urlpatterns = [
  path("latest-books/", views.LatestBookList.as_view()),
]