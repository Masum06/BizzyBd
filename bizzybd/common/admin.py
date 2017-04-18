from django.contrib import admin

from common.models import Theme, Website, Div, Page


class ThemeAdmin(admin.ModelAdmin):
    pass


class WebsiteAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'sequence_no', 'theme', 'website')


class DivAdmin(admin.ModelAdmin):
    list_display = ('website', 'theme', 'page', 'sequence_no', 'get_name', 'image', 'file')


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Div, DivAdmin)
