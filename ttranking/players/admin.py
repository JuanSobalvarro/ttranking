# ttranking/players/admin.py

from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'alias', 'gender', 'date_of_birth', 'nationality', 'ranking', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'alias', 'nationality')
    list_filter = ('gender', 'nationality')
    ordering = ('-ranking', 'last_name')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Player, PlayerAdmin)