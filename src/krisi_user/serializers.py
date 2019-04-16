from rest_framework import serializers # imported serializers fror rest framework
from rest_framework.exceptions import ValidationError
from .models import krisi_user # added Model from model.py

#class for krisi_user serializer
class krisi_user_searializers(serializers.ModelSerializer):

    # meta class for field which we want to show


    class Meta:
        model = krisi_user
        fields = ('full_name','email')


    # def validate(self,data):
    #
    #     full_name = data['full_name']
    #     email = data['email']
    #     user_qs = krisi_user.objects.filter(full_name=full_name,email=email)
    #
    #     if user_qs.exists():
    #         raise ValidationError("This email already registered.")
    #
    #     return data





