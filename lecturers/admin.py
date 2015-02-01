from django.contrib import admin

# Register your models here.
from .models import Lecturer, LecturerImage, LecturerAttribute
#from rates.models import Rate
from institutions.models import Institution


class LecturerAdmin(admin.ModelAdmin):
    
    def lecturer_institute(self, obj):
        return obj.university.abr
    lecturer_institute.admin_order_field  = 'abr'  #Allows column order sorting
    lecturer_institute.short_description = 'ABR'  #Renames column head
    
    
    #def lecturer_rate(self, obj):
    #    return obj.rates
    #lecturer_rate.admin_order_field  = 'rates'  #Allows column order sorting
    #lecturer_rate.short_description = 'Rate'  #Renames column head
    
    
    search_fields = ['firstName', 'lastName', 'title']
    list_display = ['title','__unicode__', 'department','currentPosition', 'lecturer_institute', 'rate', 'active', 'updated_Timestamp']
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
        
        
class LecturerAttributeAdmin(admin.ModelAdmin):
    
    list_display = ['__unicode__', 'updated_Timestamp']
    class Meta:
        model= LecturerAttribute        

admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(LecturerImage, LecturerImageAdmin)
admin.site.register(LecturerAttribute, LecturerAttributeAdmin)
    
