from django.db import models
from django.db.models import Model
# Create your models here.

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 200, null = True, blank = True)
    views = models.IntegerField()
    url = models.URLField(max_length = 200)
    image = models.ImageField()