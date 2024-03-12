from django.contrib import admin
from django.urls import path
from django_graphql_sports.app import views

urlpatterns = [
    path('', views.main, name='main'),
    path('football/', views.football, name='football'),
    path('basketball/', views.basketball, name='basketball'),
    path('admin/', admin.site.urls),
]