from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from channel.models import Channel, Community


class ChannelAdmin(ImportExportModelAdmin):
    list_display = ["channel_name", "user" ,"status"]

class CommunityAdmin(ImportExportModelAdmin):
    list_display = ["channel","status"]


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Community, CommunityAdmin)
