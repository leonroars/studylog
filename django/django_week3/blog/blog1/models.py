from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()

# Create your models here.
