from django.db import models
from lecturers.models import Lecturer
from datetime import datetime, timedelta
from pytz import timezone
#import pytz

# Create your models here.



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

CLARITY_CHOICE = (
    ('1', 'Not so Clear'),
    ('2', 'Manageably clear'),
    ('3', 'Clear to most'),
    ('4', 'Very Clear'),
)

HOT_CHOICE = (
    ('1', 'No'),
    ('2', 'Yes, Hot but manageble'),
    ('3', 'Yes, Mehn very hot'),
)

HANDOUT_CHOICE = (
    ('1', 'Yes, and you must buy'),
    ('2', 'Yes, but not compulsory'),
    ('3', 'No, any textbook is fine'),
)

RECOMMEND_CHOICE = (
    ('1', 'Never'),
    ('2', 'No choice'),
    ('3', 'Yes, will recommend'),
    ('4', 'Yes, strongly recommend'),
)
class Rating(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    rating = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, null=False, editable=True)
    rating_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name= "Updated")
    
    helpfulness = models.CharField(choices=HELP_CHOICE, max_length= 1, null=False, blank=False, help_text='How helpful?', verbose_name="Helpfulness", default=1)
    knowlegdeable = models.CharField(choices=KNOW_CHOICE, max_length= 1, null=False, blank=False, help_text='Knowledgeable of speciality?', verbose_name="Knowledgeable", default=1)
    clarity = models.CharField(choices=CLARITY_CHOICE, max_length= 1, null=False, blank=False, help_text='How clear is he/she', verbose_name="Clarity", default=1)
    hotness = models.CharField(choices=HOT_CHOICE, max_length= 1, null=False, blank=False, help_text='This lecturer is hot and difficult', verbose_name="How HOT?", default=1)
    handout = models.CharField(choices=HANDOUT_CHOICE, max_length= 1, null=False, blank=False,  help_text='Do you depend on Handouts, and not Textbooks', verbose_name="Handout use", default=1)
    course = models.CharField(max_length= 10, null=True, blank=True,  help_text='What course did you take with him/her', verbose_name="Course")
    recommend = models.CharField(choices=RECOMMEND_CHOICE, max_length= 1, null=False, blank=False, help_text='Will you recommend lecturer?', verbose_name="Recommend", default=1)
    describe = models.TextField(verbose_name="160 Character description", max_length=160, null=False, blank=False, default="Enter just 160 character description of your lecturer")
    
    #use get_helpfulness_display() method to get the text
    def __unicode__(self):
        return unicode(self.rating)
    
    def get_rating_time(self):
        return unicode(self.rating_time)
    
    #for more info about aggregates, see https://docs.djangoproject.com/en/1.7/topics/db/aggregation/
    def get_help(id):
        rates = Rating.objects.filter(id=id)
        for rate in rates:
            print rate.helpfulness
    
    def calc_rate(self):
         return self.helpfulness.count()
    
#class Rate(models.Model):
#    rates = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, null=False, editable=True)
#    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#    def __unicode__(self):
#        return unicode(self.rates)