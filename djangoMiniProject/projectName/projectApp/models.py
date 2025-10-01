from django.db import models

class FacultyDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"