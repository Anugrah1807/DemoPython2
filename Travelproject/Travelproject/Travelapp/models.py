from django.db import models

# Create your models here.
class states(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')
    desc=models.TextField()

class ourteam(models.Model):
    names = models.CharField(max_length=200)
    images = models.ImageField(upload_to='images')
    descr = models.TextField()




