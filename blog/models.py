from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()



    # Removes the default blog post names to real post titles in admin area. 
    def __str__(self):
       return self.title
    