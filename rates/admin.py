from django.contrib import admin
from .models import Rate, Rating

# Register your models here.

class RateAdmin:
    list_display = ['lecturer', 'currentRate']
    class Meta:
        model=Rate
    
    

class RatingAdmin:
    list_display = ['lecturer', 'rating']
    class Meta:
        model=Rate
        
        
admin.site.register(Rate, RateAdmin)
admin.site.register(Rating, RatingAdmin)