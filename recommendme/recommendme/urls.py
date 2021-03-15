"""recommendme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from reco import views
from django.conf.urls import include,url

urlpatterns = [
    # when nothing is given redirect to the home page
    path('',views.index,name='index'),
    # when /form is added redirect to the home page
    path('form',views.formPage,name='formPage'),
    # when /result is added redirect to result page
    path('result',views.result,name='result'),
    # when /admin is added go to admin.site.urls
    path('admin/', admin.site.urls),
]
