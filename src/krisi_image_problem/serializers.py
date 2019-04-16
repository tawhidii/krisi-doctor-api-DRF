from rest_framework import serializers
#from rest_framework.exceptions import ValidationError

from .models import problem_image

class problem_image_serializer(serializers.ModelSerializer):


    class Meta:
        model = problem_image
        fields = ('full_name','email','image','phone')