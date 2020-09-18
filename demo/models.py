from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)

    description = models.TextField(max_length=256, blank=True)

    price= models.FloatField(default=0, max_length=36)

    published = models.DateField(blank=True, null=True, default=None)

    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)
    
    