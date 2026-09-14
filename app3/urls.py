from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('updates/', views.updates, name='updates'),
    path('details/', views.details, name='details'),
]