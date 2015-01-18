from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Lecturer(models.Model):
    #l_ID=models.IntegerField(primary_key=True)
    
    #profiles of lecturers
    title= models.CharField(max_length=60, null=True, blank=True)
    firstName= models.CharField(max_length=120, null=False, blank=False)
    middleName= models.CharField(max_length=120, null=True, blank=True)
    lastName= models.CharField(max_length=120, null=False, blank=False)
    
    #image
    #image = models.ImageField(upload_to=PS_IMAGES)
    #i=models.ImageField(upload_to=/ps_images/)
    
    #University
    currentPosition = models.CharField(max_length=120, null=True, blank=True)
    #formerPosition = models.CharField(max_length=120, null=True, blank=True)
    #departmentID = models.CharField(max_length=120, null=True, blank=True)
    #ministry = models.CharField(max_length=120, null=True, blank=True)
    #startAtMinistry = models.DateField(null=True, blank=True)
    #endAtMinistry = models.DateField(null=True, blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_Timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.firstName) + " " + smart_unicode(self.lastName)