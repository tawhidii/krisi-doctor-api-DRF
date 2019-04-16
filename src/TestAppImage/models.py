
from django.db import models




class Test_image(models.Model):

    files = models.ImageField(upload_to='images/')




    def __str__(self):
        return self.files

