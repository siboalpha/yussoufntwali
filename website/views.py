from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    thoughts = Thought.objects.all()
    youtubelinks = YoutubeLink.objects.all()

    context = {'thoughts':thoughts, 'youtubelinks':youtubelinks}
    return render(request, 'index.html', context)