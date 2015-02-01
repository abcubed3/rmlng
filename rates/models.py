from django.db import models
from lecturers.models import Lecturer
from datetime import datetime, timedelta
from pytz import timezone
#import pytz

# Create your models here.

#class Rate(models.Model):
#    rates = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, null=False, editable=True)
#    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#    def __unicode__(self):
#        return unicode(self.rates)

HELP_CHOICE = {
    ('1', 'Not Helpful'),
    ('2', 'Somewhat Helpful'),
    ('3', 'Helpful'),
    ('4', 'Very Helpful'),
    ('5', 'Awesomely Helful'),
}
KNOW_CHOICE = (
    ('1', 'Knows it, just to teach'),
    ('2', 'Knows it well'),
    ('3', 'Knows it and can teach it'),
)
    
class Rating(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    rating = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, null=False, editable=True)
    rating_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name= "Updated")
    
    helpfulness = models.CharField(choices=HELP_CHOICE, max_length= 1, null=False, blank=False, verbose_name="How helpful?")
    knowlegdeable = models.CharField(choices=KNOW_CHOICE, max_length= 1, null=False, blank=False, verbose_name="Knowledgeable of speciality?")
    #use get_helpfulness_display() method to get the text
    def __unicode__(self):
        return unicode(self.rating)
    
    def get_rating_time(self):
        return unicode(self.rating_time)
    
    def get_help(self):
        return unicode(self.helpfulness)
    