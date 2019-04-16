
from django.contrib import admin

from .models import problem_image

# Registering Model to admin



class KrisiAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','image')

admin.site.register(problem_image,KrisiAdmin)