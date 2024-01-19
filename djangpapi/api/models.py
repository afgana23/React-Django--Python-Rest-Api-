from django.db import models

# Create your models here.
class Customer(models.Model):
    
      GENDER = [
        ("M", "MALE"),
        ("F", "FEMALE"),
    
    ]
      c_name=models.CharField(max_length=50)
      phone=models.IntegerField()
      age=models.IntegerField(blank=True,null=True)
      gender = models.CharField(blank=True,null=True, max_length=1, choices=GENDER)
      address=models.CharField(max_length=50)
   
      def __str__(self):
        return self. c_name
        
