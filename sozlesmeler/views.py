from django.shortcuts import render,get_object_or_404
from .models import Limak_Sirket, Firma, Sozlesme

def index(request):

    return render(request, 'index.html')

def detail(request):

    return render(request, 'detail.html')
