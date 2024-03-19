"""
URL configuration for stat_wanted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    ## 홈
    path('', Home.as_view(), name='home'),
    path('intro/', Introduce.as_view(), name='introduce'),


    path('my_page/', include('my_page.urls', namespace='my_page')),
    path('my_skill/', include('my_skill.urls', namespace='my_skill')),
    path('recruit/', include('recruit.urls', namespace='recruit')),
]
