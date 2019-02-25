from django.contrib import admin

# Register your models here.
from .models import Moviee, Cast, Detai,Movie

class ChoiceInline(admin.StackedInline):
	model = Cast
	extra = 3

class DetailInline(admin.StackedInline):
	model = Detai
	extra = 1

class MovieInline(admin.StackedInline):
	model = Movie
	extra = 3


class MovieeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'mdate','rating','mtype', 'director','murl','movietime','description','maincast','body','ytube','quality']}),
		
	]
	inlines = [ChoiceInline,DetailInline,MovieInline]
	list_display = ('name', 'mdate')
	list_display_links =('id','name','director')
	list_display = ('id','name', 'mdate','rating','director')
	list_filter = ['mdate','mtype','director', 'rating']
	search_fields = ['name','director','mtype']
    #date_hierarchy = ['pub_date']


class CastAdmin(admin.ModelAdmin):
	list_display = ('name', 'cname')
	list_display = ('name', 'cname','cmname','role')
	list_filter = ['name']
	search_fields = ['name', 'cname']

admin.site.register(Moviee, MovieeAdmin)
admin.site.register(Cast,CastAdmin)
admin.site.register(Detai)
admin.site.register(Movie)
