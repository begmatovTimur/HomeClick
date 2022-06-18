from django.shortcuts import render
from .models import Estate


def index(request):
    estates = Estate.objects.all()
    return render(request, "index.html", {'estates': estates})