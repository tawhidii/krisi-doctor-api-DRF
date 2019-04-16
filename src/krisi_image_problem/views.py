from django.shortcuts import render
from rest_framework import viewsets

from .models import problem_image

from .serializers import problem_image_serializer

class problem_image_view(viewsets.ModelViewSet):
    queryset = problem_image.objects.all()
    serializer_class = problem_image_serializer



