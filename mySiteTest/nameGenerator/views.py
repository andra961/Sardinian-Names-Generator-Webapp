from django.shortcuts import render
from django.http import HttpResponse
from lib import ultimale_gen_script


# Create your views here.


def home(request):
    return render(request, 'nameGenerator/home.html')
