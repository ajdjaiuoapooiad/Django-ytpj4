from django.shortcuts import render

from core.models import Video

def index(request):
    video = Video.objects.filter(visibility='public')
    context = {
        'video' : video,
    }
    return render(request, "index.html",context)
    