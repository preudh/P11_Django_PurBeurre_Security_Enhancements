"""P8_Django_Purbeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include  # Functions for use in URLsconfs
# admin.autodiscover()

urlpatterns = [
    # '' means home page, when someone goes to home page the controller will go to app_manage app here we have urls.py
    path('', include('app_manage.urls')),
    path('', include('app_users.urls')),
    path('admin/', admin.site.urls),
]
