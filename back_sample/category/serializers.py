# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category", "added_by", "date_added", "description", "slug"]