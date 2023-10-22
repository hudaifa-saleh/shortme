from django.contrib import admin

from shortme.link.models import ShortMe


class ShortMeAdmin(admin.ModelAdmin):
    list_display = ["url", 'id', "shortcode", "active"]


admin.site.register(ShortMe, ShortMeAdmin)
