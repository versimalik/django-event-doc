from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(
        to='Event',
        on_delete=models.CASCADE
    )
    
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.photo).split("/")[-1]