from django.urls import path
from channel import views


urlpatterns = [
    path("<channel_name>/", views.channel_profile, name="channel-profile"),
    path("<channel_name>/video/", views.channel_videos, name="channel-videos"),
    path("<channel_name>/community/", views.channel_community, name="channel-community"),
    path("<channel_name>/community/<int:community_id>", views.channel_community_detail, name="channel-community-detail"),

    # Create COmment URL
    path("community/<int:community_id>/create-comment/", views.create_comment, name="community-create-comment"),

    # Delete Comment URL
    path("community/<int:community_id>/<int:comment_id>/", views.delete_comment, name="community-delete-comment"),




]