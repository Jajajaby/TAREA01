from django.contrib import admin
from tarea01.models import Team, Player, Coach, BasketGame

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo', 'code')
    search_fields = ['name', 'code']
    def _thumbnail(self,obj):
    	if obj.logo:
    		return mark_safe(u'<img src="/media/%s" alt="" width="25" height="25" />' % (obj.logo))
    	else:
    		return "[No Image]"


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'birthday', 'age', 'rut', 'email', 'height', 'weight', 'photo', 'position', 'team')
    search_fields = ['name', 'nickname', 'rut', 'team']
    list_filter = ('team', 'birthday')
    def _thumbnail(self,obj):
    	if obj.photo:
    		return mark_safe(u'<img src="/media/%s" alt="" width="25" height="25" />' % (obj.photo))
    	else:
    		return "[No Image]"


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'email', 'rut', 'nickname')


@admin.register(BasketGame)
class BasketGame(admin.ModelAdmin):
	list_display = ('name', 'name')