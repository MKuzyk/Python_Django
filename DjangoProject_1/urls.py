"""
URL configuration for django_project_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path

urlpatterns = [
    #    path('admin/', admin.site.urls),

]

from django.urls import path
from . import views

urlpatterns = [
    path('call-count/', views.call_count),
    path('current-time/', views.current_time),
    path('country/<str:country_name>/', views.country_by_name, name='country_by_name_url'),
    path('country-one/json/<str:country_name>/', views.country_name, name='country_name'),
    path('country/<str:country_name>/', views.country, name='country_name'),
    path('country/index/<int:country_index>/', views.country_by_index, name='country_index'),
    path('first-html/',views.first_html,name='first_html'),
    path('country-list/<int:max_countries>/', views.country_list, name='country_list_url'),
    path('country-list-json/<int:max_countries>/', views.country_list_json, name='country_list'),
    path('first-template/', views.first_template, name='first_template'),
]
