from django.db import models

class Day(models.Model):
   
    fajr=models.CharField(max_length=100,null=True,blank=True)
    dohr=models.CharField(max_length=100,null=True,blank=True)
    aser=models.CharField(max_length=100,null=True,blank=True)
    maghrib=models.CharField(max_length=100,null=True,blank=True)
    aisha=models.CharField(max_length=100,null=True,blank=True)
    moha=models.
    def __str__(self):
        return str(self.id)
    
