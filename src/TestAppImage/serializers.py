from rest_framework import serializers
#from rest_framework.exceptions import ValidationError

from .models import Test_image

class test_image_serializer(serializers.ModelSerializer):


    class Meta:
        model = Test_image
        fields = '__all__'