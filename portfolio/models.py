from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=100)
    desription= models.CharField(max_length=500)
    #image= models.ImageField(upload_to='portfolio/images/',blank=True)
    #document = models.FileField(upload_to='portfolio/documents/', blank=True)
    #url= models.URLField(blank=True)
