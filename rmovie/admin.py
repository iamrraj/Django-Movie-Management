from django.contrib import admin

# Register your models here.
from .models import Moviee, Cast, Detai

class ChoiceInline(admin.StackedInline):
	model = Cast
	extra = 3

class DetailInline(admin.StackedInline):
	model = Detai
	extra = 1


class MovieeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'mdate','rating','mtype', 'director','murl','movietime','description','maincast','body','ytube']}),
		
	]
	inlines = [ChoiceInline,DetailInline]
	list_display = ('name', 'mdate')
	list_display = ('id','name', 'mdate','rating','director')
	list_filter = ['mdate','mtype','director', 'rating']
	search_fields = ['name','director','mtype']
    #date_hierarchy = ['pub_date']

admin.site.register(Moviee, MovieeAdmin)
admin.site.register(Cast)
admin.site.register(Detai)