from django.contrib import admin

from urls.models import Collection, Url


admin.site.register(Collection)


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'user', 'created_at', 'updated_at')

