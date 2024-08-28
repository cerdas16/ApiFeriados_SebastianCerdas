from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .api.views import ListHolidays

objectrouter = DefaultRouter()
#objectrouter.register('api_holidays_list', HolidaysViewSet, basename='api_holidays')

urlpatterns = [
    path('', views.index, name="home"),
    path('list_holidays', ListHolidays.as_view(), name="apiview_holidays"),
    path('list_holidays_view', views.load_holidays, name="list_holidays_view")
]