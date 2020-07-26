from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor

def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    return render(request,'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtor= Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }

    return render(request,'pages/about.html', context)