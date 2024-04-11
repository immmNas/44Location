from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('contact_us', views.contact_us, name='contact_us'),


]