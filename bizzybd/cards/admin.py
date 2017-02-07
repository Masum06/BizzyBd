from django.contrib import admin
from cards.models import Themes, Cards


class ThemesAdmin(admin.ModelAdmin):
    pass


class CardsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Themes, ThemesAdmin)
admin.site.register(Cards, CardsAdmin)