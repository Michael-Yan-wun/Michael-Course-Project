from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'teacher', 'loc', 'content', 'date', 'img', 'online', 'sys')
