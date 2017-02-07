from django.contrib import admin
from cards.models import Themes


class ThemesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Themes, ThemesAdmin)
