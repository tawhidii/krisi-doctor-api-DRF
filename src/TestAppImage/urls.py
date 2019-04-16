from django.urls import path , include

from . import views

from rest_framework import routers

#image_router = routers.DefaultRouter('api/image/v1.0',views.problem_image_view)

router = routers.DefaultRouter()
router.register('image',views.test_image_view)
urlpatterns = [

    path('',include(router.urls)),

]