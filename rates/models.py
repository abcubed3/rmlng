from django.db import models
from lecturers.models import Lecturer
# Create your models here.

class Rate(models.Model):
    lecturer = models.ManyToManyField(Lecturer)
    currentRate = models.IntegerField(editable=True, default=0.00, max_length=3, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_Timestamp = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name= "Updated")
    
    
    def __unicode__(self):
        return self.currentRate
    
    
class Rating(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    rate = models.ForeignKey(Rate)
    rating = models.IntegerField(editable=True, default=0.00, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
 
    def __unicode__(self):
        return self.rating
        
    
    