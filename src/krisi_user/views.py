from django.shortcuts import render

from rest_framework import viewsets


'''importing krisi_user model and serializers 
in the views file '''

from .models import krisi_user
from .serializers import krisi_user_searializers


#class for krisi_user_view

class krisi_user_view(viewsets.ModelViewSet):
    queryset = krisi_user.objects.all()
    serializer_class = krisi_user_searializers

