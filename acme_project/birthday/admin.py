from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    search_fields = ('last_name', 'first_name',)
    list_display_links = ('last_name', 'first_name',)


admin.site.register(Birthday, BirthdayAdmin)
