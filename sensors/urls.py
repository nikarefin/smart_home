from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

route = DefaultRouter()

route.register(r'sensors', SensorsViewSet)
route.register(r'measurements', MeasurementsViewSet)

urlpatterns = route.urls
