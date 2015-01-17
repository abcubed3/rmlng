from django.contrib import admin

# Register your models here.
from .models import Lecturer


class LecturerAdmin(admin.ModelAdmin):
    class Meta:
        model= Lecturer
        

admin.site.register(Lecturer, LecturerAdmin)
    
