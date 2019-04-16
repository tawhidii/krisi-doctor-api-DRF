from django.contrib import admin

from .models import krisi_user

# Registering Model to admin



class KrisiAdmin(admin.ModelAdmin):
    list_display = ('full_name','email')

admin.site.register(krisi_user,KrisiAdmin)
