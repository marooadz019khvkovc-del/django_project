from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('pricing/', views.pricing, name='pricing'),
    path('order/', views.order, name='order'),
]