from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('moviee/', views.MovieApiView.as_view(), name='list'),
    path('moviee/<int:pk>/',views.MovieDetailAPIView.as_view(), name='detail'),

    path('cast/', views.CastApiView.as_view(), name='list'),
    path('cast/<int:pk>/',views.CastDetailAPIView.as_view(), name='detail'),

    path('detail/', views.DetailApiView.as_view(), name='list'),
    path('detail/<int:pk>/',views.DetailDetailAPIView.as_view(), name='detail'),
    # path('Movie/<int:pk>/edit', views.MovieUpdateAPIView.as_view(), name='update'),

    path('movie/', views.customers_list),
    path('movie/<int:pk>/', views.customers_detail), 
    
]
