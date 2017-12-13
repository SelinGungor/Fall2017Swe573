"""swe573 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core import views as core_views
from swe573 import views as swe573_views

from personal import views as personal_views

urlpatterns = [
    #url(r'^core/', include('core.urls')),
    url(r'^$', core_views.post_create, name='home'),
    #url(r'^$', core_views.home, name='home'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), #important for twitter login
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^contact/$', swe573_views.contact, name='contact_info'),
    url(r'^about_deepyou/$', swe573_views.about_deepyou, name='about_deepyou'),
    #url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^admin/', admin.site.urls),
    url(r'^personal/', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
]