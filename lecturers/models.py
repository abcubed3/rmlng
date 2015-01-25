from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Lecturer(models.Model):
    
    #profiles of lecturers
    title= models.CharField(max_length=12, null=True, blank=True)
    firstName= models.CharField(max_length=120, null=False, blank=False)
    middleName= models.CharField(max_length=120, null=True, blank=True)
    lastName= models.CharField(max_length=120, null=False, blank=False)
    
    #University
    department = models.CharField(max_length = 120, null= True, blank=True, verbose_name ="Department")
    currentPosition = models.CharField(max_length=120, null=True, blank=True, verbose_name= "Current Position")
    #formerPosition = models.CharField(max_length=120, null=True, blank=True)
    #departmentID = models.CharField(max_length=120, null=True, blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_Timestamp = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name= "Updated")
    
    active = models.BooleanField(default=True)
    slug = models.SlugField()
    
    def __unicode__(self):
        return smart_unicode(self.firstName) + " " + smart_unicode(self.lastName)
    
class LecturerImage(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    image = models.ImageField(upload_to='lecturers/images/', verbose_name='Image', null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_Timestamp = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name= "Updated")
    
    def __unicode__(self):
        return self.lecturer.firstName + " "+ self.lecturer.lastName