from django.contrib import admin

# Register your models here.
from .models import Institution, InstitutionImage


class InstitutionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location', 'abr']
    list_display = ['__unicode__', 'vc', 'established', 'formerName', 'former','active', 'updated_Timestamp']
    list_editable = ['active', 'vc', 'former', 'formerName']
    list_filter = ['former', 'active']
    date_hierarchy = 'timestamp'
    readonly_fields = ['timestamp', 'updated_Timestamp']
    prepopulated_fields = {"slug" : ("name",) }
    class Meta:
        model= Institution
        
class InstitutionImageAdmin(admin.ModelAdmin):
    
     class Meta:
        model= InstitutionImage
        
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(InstitutionImage, InstitutionImageAdmin)
    
