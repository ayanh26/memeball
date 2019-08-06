from django.db import models

# Create your models here.

class post(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=20)
    summary = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
