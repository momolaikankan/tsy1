from rest_framework import serializers
from api import models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"