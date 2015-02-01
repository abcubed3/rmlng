from django.db import models
from lecturers.models import Lecturer

# Create your models here.

#class Rate(models.Model):
#    rates = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, null=False, editable=True)
#    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#    def __unicode__(self):
#        return unicode(self.rates)
    
    
class Rating(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    rating = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, null=False, editable=True)
    rating_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name= "Updated")
    
    def __unicode__(self):
        return unicode(self.rating)
    
    def get_rating_time(self):
        return unicode(self.rating_time)
    