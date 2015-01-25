from django.contrib import admin

# Register your models here.
from .models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'lastName', 'abr']
    list_display = ['__unicode__', 'abr', 'established']
    class Meta:
        model= Institution
        

admin.site.register(Institution, InstitutionAdmin)
    
