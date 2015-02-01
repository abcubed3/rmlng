from django.contrib import admin
from .models import Rating #Rate 
from lecturers.models import Lecturer

# Register your models here.

#class RateAdmin(admin.ModelAdmin):
#    def get_lecturer(self, obj):
#        return obj.rates
#    get_lecturer.admin_order_field  = 'lecturer'  #Allows column order sorting
#    get_lecturer.short_description = 'Lecturer'  #Renames column head
#    
#    list_display = ['get_lecturer', 'rates']
#    #'get_lecturer',
#    class Meta:
#        model= Rate
#    
    

class RatingAdmin(admin.ModelAdmin):
    def get_lecturer(self, obj):
        return obj.lecturer  
    get_lecturer.admin_order_field  = 'lecturer'  #Allows column order sorting
    get_lecturer.short_description = 'Lecturer'  #Renames column head
    
    search_fields = ['get_lecturer', 'rating']
    list_filter = ['rating_time', 'rating']
    date_hierarchy = 'rating_time'
    
    list_display = ['get_lecturer', 'rating', 'rating_time']
    class Meta:
        model=Rating
        
        
#admin.site.register(Rate, RateAdmin)
admin.site.register(Rating, RatingAdmin)