
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from channel.models import Channel
from core.models import Video


def channel_profile(request,channel_name):
    channel = get_object_or_404(Channel,id=channel_name)
    videos = Video.objects.filter(user=channel.user, visibility="public").order_by("-views")
    
    try:
        video_featured = Video.objects.get(user=channel.user.id, featured=True)
    except:
        
        video_featured = None
        messages.warning(request,f"Only one video can featured!")
    
    context = {
        'channel': channel,
        'videos': videos,
        'video_featured':video_featured,
    }
    return render(request,"channel/channel.html",context)