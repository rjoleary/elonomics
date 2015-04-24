from django.contrib import admin
from elonomics.models import Player, Game

class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'user_name': ('full_name',)}

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game)
