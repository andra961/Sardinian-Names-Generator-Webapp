from django.shortcuts import render
from django.http import HttpResponse
from .script_lib import ultimale_gen_script


# Create your views here.


def home(request):
    namelist = ultimale_gen_script.main("1",5,"M")
    return render(request, 'nameGenerator/home.html')
