from django.contrib import admin

from common.models import Website, Div


class WebsiteAdmin(admin.ModelAdmin):
    pass


class DivAdmin(admin.ModelAdmin):
    pass


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Div, DivAdmin)
