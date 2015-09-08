"""rowanv_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

from portfolio import views

static = os.path.join( os.path.dirname(__file__), 'static' )

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    #url(r'^portfolio/windchill/', TemplateView.as_view(template_name='visualizations/windchill_table.html')),
    url(r'^portfolio/windchill/', views.windchill, name='windchill'),
    url(r'^portfolio/oecd_unemployment/', views.oecd_unemployment, name='oecd_unemployment'),
]
