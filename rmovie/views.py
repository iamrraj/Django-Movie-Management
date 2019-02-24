from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone
from .models import Moviee, Cast,Author
import datetime
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import PostForm
from django.views import generic
from django.contrib.auth.models import User
from random import sample
# from django_filters import filters

# filters.LOOKUP_TYPES = [
#     ('', '---------'),
#     ('exact', 'Is equal to'),
#     ('not_exact', 'Is not equal to'),
#     ('lt', 'Lesser than'),
#     ('gt', 'Greater than'),
#     ('gte', 'Greater than or equal to'),
#     ('lte', 'Lesser than or equal to'),
#     ('startswith', 'Starts with'),
#     ('endswith', 'Ends with'),
#     ('contains', 'Contains'),
#     ('not_contains', 'Does not contain'),
# ]

def recent(request):
    most_recent = Moviee.objects.order_by('-timestamp')[:21]
    #most_recent = Moviee.objects.all().order_by('?')[:10]
    return render(request, 'recent.html', {'most_recent': most_recent})

def upcoming(request):
    upcoming = Moviee.objects.filter('-timestamp') #[:21]
    return render(request, 'upcoming.html', {'most_recent': upcoming})



def toprated(request):
    
    contact_list = Moviee.objects.filter(rating__gte= 8) #[:21]
    search_term=''
        
    if 'q' in request.GET:
        search_term = request.GET['q']
        contact_list = contact_list.filter(Q(name__icontains=search_term)|
                                           Q(director__icontains=search_term)|
                                           Q(mtype__icontains=search_term)).distinct()
        

                        
    paginator = Paginator(contact_list, 20) # Show 4 contacts per page

    page = request.GET.get('page')
    toprated = paginator.get_page(page)
    return render(request, 'toprated.html', {'toprated': toprated})



def BlogListView(request):
     # Cast.objects.get(id=1).movie_set.all()
    time = timezone.now().date()
    most_recent = Moviee.objects.order_by('-timestamp') #[:3]
    contact_list = Moviee.objects.all()
    search_term=''
        
    if 'q' in request.GET:
        search_term = request.GET['q']
        contact_list = contact_list.filter(Q(name__icontains=search_term)|
                                           Q(director__icontains=search_term)|
                                           Q(mtype__icontains=search_term)).distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(contact_list, 16)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    # paginator = Paginator(contact_list, 20) # Show 4 contacts per page
    # page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    return render(request, 'index.html', {'users': users })


# class ProductDetailView(DetailView):
#     # context_object_name = 'book_list'
#     # most = Moviee.objects.all().order_by('?')[:10]
#     model = Moviee
#     template_name = 'moviedetail.html'


def post_detail(request, pk): #retrieve
    most_recent = Moviee.objects.all().order_by('?')[:4]
    moviee = get_object_or_404(Moviee, pk=pk)
   
    context = {
        'moviee': moviee,
        'most_recent': most_recent,
    }
    return render(request, 'moviedetail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = PostForm()
    return render(request, 'addmovie.html', {'form': form})
