"""crimecity URL Configuration

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
from django.urls import path, include
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('mainPage.urls', 'login'), name='login'),
    path('main/', include('innerMain.urls', 'main'), name='main'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('map/', include('mapPage.urls', 'map'), name='map'),
    path('chart/', include('chartPage.urls', 'chart'), name='chart'),
    path('traffic/', include('traffic.urls', 'traffic'), name='traffic'),
    path('board/', include('noteBoard.urls', 'board'), name='board'),

]
