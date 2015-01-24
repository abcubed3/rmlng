from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Institution(models.Model):
    #inst_id = models.AutoField(primary_key=True)
    
    #Profiles of institutions
    #Abr - Abbrevation 
    abr= models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    former = models.BooleanField(default = False, verbose_name="Former Name")
    formerName= models.CharField(max_length=120, null=True, blank=True)
    nickName = models.CharField(max_length=120, null=True, blank=True)
    motto = models.CharField(max_length=120, null=True, blank=True)
    
    
    established = models.DateField()
    #schoolType = models.ChoiceField("Public", "Private", "Unknown")
    #schoolType= models.BooleanField("Public", "Private", "Unknown")
    vc = models.CharField(max_length =120, null=True, blank=True)
    #students = models.IntegerField(max_length= 10)
    
    #image
    #image = models.ImageField(upload_to=PS_IMAGES)
    #i=models.ImageField(upload_to=/ps_images/)
    location = models.CharField(max_length=120, null=False, blank=False)
    #campus = models.BooleanField("Urban", "Rural", "Suburban")
    colors = models.CharField(max_length=120)
    
    website = models.URLField()
    
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_Timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name) + " " + smart_unicode(self.location)