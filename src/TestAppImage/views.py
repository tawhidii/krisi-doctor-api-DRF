from django.shortcuts import render
from rest_framework import viewsets

from .models import Test_image

from .serializers import test_image_serializer

class test_image_view(viewsets.ModelViewSet):
    queryset = Test_image.objects.all()
    serializer_class = test_image_serializer
