from django.contrib import admin

# Register your models here.
from .models import Lecturer


class LecturerAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'lastName', 'title']
    
    list_display = ['__unicode__', 'currentPosition']
    class Meta:
        model= Lecturer
        

admin.site.register(Lecturer, LecturerAdmin)
    
