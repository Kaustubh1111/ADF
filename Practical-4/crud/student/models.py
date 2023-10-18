from django.db import models

# Create your models here.
class studentDetails(models.Model):
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30,null=True)
    lname = models.CharField(max_length=30,blank=True)
    image = models.ImageField(upload_to='uploads/img/')
    email = models.EmailField(max_length=255)
    resume = models.FileField(upload_to='uploads/',help_text="PLease upload your latest resume")
    cgpa = models.FloatField()
    ugDuration = models.DurationField()
    url = models.URLField(max_length=200)
    dob = models.DateField()
