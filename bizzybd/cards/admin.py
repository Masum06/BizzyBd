from django.contrib import admin
from cards.models import Themes, Cards


class ThemesAdmin(admin.ModelAdmin):
    # list_filter = ('is_theme',)

    def get_queryset(self, request):
        qs = super(ThemesAdmin, self).get_queryset(request)
        qs = qs.filter(is_theme=True)
        return qs


class CardsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Themes, ThemesAdmin)
admin.site.register(Cards, CardsAdmin)
