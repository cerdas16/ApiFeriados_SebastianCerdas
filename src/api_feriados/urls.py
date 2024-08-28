"""
URL configuration for api_feriados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from djgentelella.urls import urlpatterns as urls_djgentelella
from feriados.urls import urlpatterns as admin_urls

urlpatterns = urls_djgentelella + [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('holidays:home')), name='home'),
    path('holidays/', include((admin_urls, 'holidays'), namespace="holidays"))
]
