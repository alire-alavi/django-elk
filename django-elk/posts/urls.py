from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("test/", views.ErrorView.as_view()),
]