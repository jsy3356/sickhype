from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Hypebeast
from .forms import HyperForm

def index(request):
    context = {'hypebeasts' : Hypebeast.objects.all()}
    return render(request, 'hypebeasts/index.html', context)

def hyper(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HyperForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Thanks for being hypebeasts.")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HyperForm()

    return render(request, 'hypebeasts/hyper.html', {'form': form})