from django.contrib import admin

from common.models import Website


class WebsiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Website, WebsiteAdmin)