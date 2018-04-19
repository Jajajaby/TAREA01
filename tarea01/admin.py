from django.contrib import admin
from tarea01.models import Team, Player, Coach, SoccerGame

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'code') # ('name', 'description', 'logo', 'code') 


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'birthday', 'age', 'rut') #('name', 'nickname', 'birthday', 'age', 'rut', 'email', 'height', 'weight', 'photo', 'position')
    #list_filter = ('album', 'duration')


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'email', 'rut', 'nickname')


@admin.register(SoccerGame)
class SoccerGame(admin.ModelAdmin):
	list_display = ('name', 'name')