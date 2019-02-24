from django.urls import path
from . import views

#from .views import (BlogDetailView)
# SET THE NAMESPACE!
app_name = 'rmovie'

urlpatterns = [

    path('', views.BlogListView, name='product'),
    path('recentmovie', views.recent, name='recent'),
    # path('movie/list/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('movie/list/<int:pk>/', views.post_detail, name='product_detail'),
    path('create', views.post_create, name='create'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('toprated', views.toprated, name='toprated'),
    
]
