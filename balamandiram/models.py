from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length= 50)
    date = models.DateField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')

def __str__(self):
    return self.title
