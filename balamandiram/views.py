from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def setup(request):
    return render(request, 'balamandiram/setup.html')

def gallery(request):
    return render(request, 'balamandiram/gallery.html', {'posts': Gallery.objects.all()})