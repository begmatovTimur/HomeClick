from django.shortcuts import render, redirect
from .models import Estate, Category, Photo
from django.db.models import Q
from .estate_form import EstateForm

def index(request):
    estates = Estate.objects.all()
    search_estates = request.GET.get("search")
    if search_estates:
        estates = Estate.objects.filter(Q(price__icontains=search_estates) | Q(description__icontains=search_estates))
        
    categories = Category.objects.all()
    return render(request, "index.html", {'estates': estates, 'categories': categories})


def map(request):
    return render(request, "map.html")

def estate_detail(request, pk):
    estate = Estate.objects.get(pk=pk)
    photos = Photo.objects.filter(estate__pk=pk)
    return render(request, 'estate_detail.html', {'estate': estate, 'photos': photos})


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def add_estate(request):
    form = EstateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'add_estate.html', {'form':form})