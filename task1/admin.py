from django.contrib import admin
from .models import Game, Buyer

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('title', 'cost', 'size')  # Отображаем поля title, cost и size
	list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
	search_fields = ('title',)  # Поиск по полю title
	list_per_page = 20  # Ограничение кол-ва записей до 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
	list_display = ('name', 'balance', 'age')  # Отображаем поля name, balance и age
	list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
	search_fields = ('name',)  # Поиск по полю name
	list_per_page = 30  # Ограничение кол-ва записей до 30
	readonly_fields = ('balance',)  # Поле balance доступно только для чтения

# Register your models here.
