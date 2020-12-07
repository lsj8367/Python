"""django_test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from gpapp import views
from gpapp.views import MyCallView
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.MainFunc, name = 'MainFunc'), # Function views
    path('gpapp/callget/', MyCallView.as_view()), # Class-based views
    path('gpapp/', include('gpapp.urls')) # Including another URLconf gpapp.urls에게 위임
    
]
