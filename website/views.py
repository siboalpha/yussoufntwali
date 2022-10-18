from django.shortcuts import render
from .models import Thought, YoutubeLink
# Create your views here.
def index(request):
    thoughts = Thought.objects.order_by("-date_created")[:8]
    youtubelinks = YoutubeLink.objects.order_by("-date_created")[:8]

    context = {'thoughts':thoughts, 'youtubelinks':youtubelinks}

    print(youtubelinks.count)
    return render(request, 'index.html', context)