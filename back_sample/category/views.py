from django.shortcuts import render

# Create your views here.

# todo/todo_api/views.py
from rest_framework.views import APIView, Response, status
from rest_framework import permissions
from .models import Category
from .serializers import CategorySerializer
from django.http import HttpResponse, HttpResponseNotFound


class CategoryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Category.objects.all()
        serializer = CategorySerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'category': request.data.get('category'), 
            'added_by': request.data.get('added_by'), 
            'description': request.data.get('description')
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("wrong data format / data")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)