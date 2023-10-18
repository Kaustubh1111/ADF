from django.db import models
# Create your models here.
#admin admin123
class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)
    description = models.TextField() 
    last_modified = models.DateTimeField(auto_now_add = True)
    email_id= models.EmailField()
    age = models.IntegerField()
    agree = models.BooleanField()
    class Meta:  
        db_table = "AppModelForm_Student" 
