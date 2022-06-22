from django.shortcuts import render
from .models import Estate, Category
from django.db.models import Q


def index(request):
    estates = Estate.objects.all()
    search_estates = request.GET.get("search")
    if search_estates:
        estates = Estate.objects.filter(Q(description__icontains=search_estates) and Q(price__icontains=search_estates) and Q(room_amount__icontains=search_estates))
        
    categories = Category.objects.all()
    return render(request, "index.html", {'estates': estates, 'categories': categories})


def map(request):
    return render(request, "map.html")

def estate_detail(request, pk):
    estate = Estate.objects.get(pk=pk)
    return render(request, 'estate_detail.html', {'estate': estate})