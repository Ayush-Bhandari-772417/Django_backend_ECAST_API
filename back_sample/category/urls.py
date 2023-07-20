# todo/todo_api/urls.py : API urls.py
# from django.conf.urls import url
from django.urls import path, include
from .views import (
    CategoryListApiView,
)

urlpatterns = [
    path('category-api', CategoryListApiView.as_view()),
]