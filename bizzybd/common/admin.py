from django.contrib import admin

from common.models import Website, Div, Page


class WebsiteAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'sequence_no', 'website')


class DivAdmin(admin.ModelAdmin):
    list_display = ('website', 'page', 'sequence_no', 'get_name', 'image', 'file')


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Div, DivAdmin)
