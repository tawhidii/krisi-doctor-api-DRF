#this is krisi_user app url

from django.urls import path , include

# import views to app url
from . import views

#importing rest framework router

from rest_framework import routers

#creating router from rest routers

router = routers.DefaultRouter()
router.register('api/user',views.krisi_user_view)  # register krisi_user_view to router


urlpatterns = [

    path('',include(router.urls))

]
