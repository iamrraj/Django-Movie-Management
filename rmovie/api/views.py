from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rmovie.models import Moviee, Cast,Detai
from .serializers import *
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.views import APIView

from drf_multiple_model.views import ObjectMultipleModelAPIView,FlatMultipleModelAPIView

class MovieApiView(generics.ListCreateAPIView):
    queryset = Moviee.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moviee.objects.all()
    serializer_class = MovieDetailsSerializer


class CastApiView(generics.ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class CastDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class = DCastSerializer
    


class DetailApiView(generics.ListCreateAPIView):
    queryset = Detai.objects.all()
    serializer_class = DetailSerializer


class DetailDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detai.objects.all()
    serializer_class = DDetailSerializer
    
    
   