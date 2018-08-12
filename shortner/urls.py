"""shortify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    #This will display the index page
    path('', views.index,name='index'),
    #The will display the page which contains the shortened URL
    path('shortenURL',views.longURL,name='shortenURL'),
    #This will serve the link for url redirection.
    url(r'^shortner/(?P<id>[a-zA-Z0-9]+)$',views.redirectExternal,name='shortner'),
]
