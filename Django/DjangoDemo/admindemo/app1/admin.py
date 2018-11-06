from django.contrib import admin
from app1.models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('id','name')
    

    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(Publisher)