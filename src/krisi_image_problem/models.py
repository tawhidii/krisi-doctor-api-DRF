
from django.db import models

from krisi_user.models import krisi_user


class problem_image(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=50)
    krisi_user = models.ForeignKey(krisi_user,on_delete= models.CASCADE,null=True)


    def __str__(self):
        return self.full_name





