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
    serializer_class = MovieDetailsSerializer1


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
    




@api_view(['GET', 'POST'])
def customers_list(request):
    """
 List  customers, or create a new customer.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Moviee.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = MovieSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        customer = Moviee.objects.get(pk=pk)
    except Moviee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieDetailsSerializer(customer,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieDetailsSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
 
   