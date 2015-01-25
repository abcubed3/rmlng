from django.contrib import admin

# Register your models here.
from .models import Lecturer, LecturerImage


class LecturerAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'lastName', 'title']
    list_display = ['title','__unicode__', 'department','currentPosition', 'active', 'updated_Timestamp']
    list_editable = [ 'active', 'department','currentPosition', 'title']
    list_display_links = ['__unicode__']
    list_filter = ['active', 'updated_Timestamp']
    date_hierarchy = 'timestamp'
    prepopulated_fields = {"slug" : ("title","lastName",) }
    readonly_fields = ['timestamp', 'updated_Timestamp']
    class Meta:
        model= Lecturer
        
class LecturerImageAdmin(admin.ModelAdmin):
    class Meta:
        model= LecturerImage

admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(LecturerImage, LecturerImageAdmin)
    
