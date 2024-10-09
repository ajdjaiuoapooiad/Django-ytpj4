from django.shortcuts import render

from core.models import Video

def index(request):
    video = Video.objects.filter(visibility='public')
    context = {
        'video' : video,
    }
    return render(request, "index.html",context)
    
def videoDetail(request, pk):
    video = Video.objects.get(id=pk)
    video.views = video.views + 1
    video.save()
    
    context = {
        'video' : video,
    }
    
    
    return render(request, "video.html",context)