from django.contrib import admin

# Register your models here.
from .models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    class Meta:
        model= Institution
        

admin.site.register(Institution, InstitutionAdmin)
    
