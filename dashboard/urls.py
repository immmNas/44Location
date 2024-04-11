from django.urls import path
from . import views



urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    path('carsList/', views.carsList, name='carsList'),
    path('customers/<str:pk>/', views.customers, name='customers'),

    path('createReservation/<str:pk>/', views.createReservation, name='createReservation'),
    path('updateReservation/<str:pk>/', views.updateReservation, name='updateReservation'),
    path('deleteReservation/<str:pk>/', views.deleteReservation, name='deleteReservation'),

]