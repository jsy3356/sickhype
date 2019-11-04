from django.shortcuts import render
from .models import Hypebeast

def index(request):
    context = {'hypebeasts' : Hypebeast.objects.all()}
    return render(request, 'hypebeasts/index.html', context)