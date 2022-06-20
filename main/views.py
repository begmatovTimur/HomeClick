from django.shortcuts import render
from .models import Estate, Category


def index(request):
    estates = Estate.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", {'estates': estates, 'categories': categories})