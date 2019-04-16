from django.db import models

# Creating krisi_user Model

class krisi_user(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
