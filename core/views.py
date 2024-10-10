
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from core.models import Comment, Video

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
    
    # Suggesting Video
    video_tags_id = video.tags.values_list("id", flat=True)
    similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    similar_videos = similar_videos.annotate(same_tags=Count("tags")).order_by("-same_tags", "-date")[:25]

    comment = Comment.objects.filter(active=True, video=video).order_by("-date")

    
    context = {
        'video' : video,
        "comment":comment,
        "similar_videos":similar_videos,
    }
    
    
    return render(request, "video.html",context)

def ajax_save_comment(request):
    if request.method == "POST":
        pk = request.POST.get("id")

        comment = request.POST.get("comment")
        video = Video.objects.get(id=pk)
        user = request.user

        new_comment = Comment.objects.create(comment=comment, user=user, video=video)
        new_comment.save()

        response = "Comment Posted"
        return HttpResponse(response)
