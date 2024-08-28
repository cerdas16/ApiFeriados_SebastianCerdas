from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


objectrouter = DefaultRouter()
#objectrouter.register('api_holidays_list', HolidaysViewSet, basename='api_holidays')

urlpatterns = [
    path('', views.index, name="home"),
]