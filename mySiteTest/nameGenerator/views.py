from django.shortcuts import render
from django.http import HttpResponse
from .script_lib import ultimale_gen_script


# Create your views here.


def home(request):
    if request.method == 'POST':
        input = request.POST
        if "quantity" in input and "vocabolario" in input and "operation" in input:
            namelist = ultimale_gen_script.main(input["operation"], int(input["quantity"]), input["vocabolario"])
            context = {"names": namelist}
            return render(request, 'nameGenerator/home.html', context)
    return render(request, 'nameGenerator/home.html')
