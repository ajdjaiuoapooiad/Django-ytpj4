from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from channel.models import Channel


class ChannelAdmin(ImportExportModelAdmin):
    list_display = ["channel_name", "user" ,"status"]


admin.site.register(Channel, ChannelAdmin)