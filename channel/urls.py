from django.urls import path
from channel import views


urlpatterns = [
    path("<channel_name>/", views.channel_profile, name="channel-profile"),
    path("<channel_name>/video/", views.channel_videos, name="channel-videos"),
    path("<channel_name>/community/", views.channel_community, name="channel-community"),
    path("<channel_name>/community/<int:community_id>", views.channel_community_detail, name="channel-community-detail"),




]