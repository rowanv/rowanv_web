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
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    #url(r'^portfolio/windchill/', TemplateView.as_view(template_name='visualizations/windchill_table.html')),
    url(r'^portfolio/windchill/', views.windchill, name='windchill'),
    url(r'^portfolio/oecd_unemployment/', views.oecd_unemployment, name='oecd_unemployment'),
    url(r'^portfolio/about/', views.about, name='about'),
    url(r'^portfolio/contact/', views.contact, name='contact'),
    url(r'^portfolio/skills/', views.skills, name='skills'),
    url(r'^portfolio/electronegativity/', views.electronegativity, name='electronegativity'),
    url(r'^portfolio/geo_twitter/', views.geo_twitter, name='geo_twitter'),
    url(r'^portfolio/research_funding/', views.research_funding, name='research_funding'),
    url(r'^portfolio/housing_prices/', views.housing_prices, name='housing_prices'),
    url(r'^portfolio/gender_olympics/', views.gender_olympics, name='gender_olympics'),
    url(r'^portfolio/gender_olympics_ipython/', views.gender_olympics_ipython,
        name='gender_olympics_ipython'),
    url(r'^portfolio/gender_olympics_viz/', views.gender_olympics_viz,
        name='gender_olympics_viz'),
    url(r'^portfolio/brazil_map/', views.brazil_map, name='brazil_map'),
    url(r'^portfolio/voter_turnout/', views.voter_turnout, name='voter_turnout'),
    url(r'^portfolio/voter_turnout_ipython/', views.voter_turnout_ipython,
        name='voter_turnout_ipython'),
    url(r'^portfolio/voter_turnout_viz/', views.voter_turnout_viz,
        name='voter_turnout_viz'),
    url(r'^portfolio/business_dash/', views.business_dash,
        name='business_dash'),
    url(r'^portfolio/resume/', views.resume, name='resume'),
]
