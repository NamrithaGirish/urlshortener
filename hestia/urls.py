"""hestia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from shorturl.views import main_view,event_view,hackathon_view,proshow_view,urlRedirect
base="hestiatkmce.live/"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view,name="home"),
    path(base,main_view,name="home"),
    path(base+"events/",event_view,name="events"),
    path(base+'events/hackathon/',hackathon_view,name="hackathon"),
    path(base+'events/shows/proshow/',proshow_view,name="proshow"),
    path(base+'<str:key>/',urlRedirect,name="redirect"),
]
