from django.db import models

# Create your models here.

class TrackerApp(models.Model):
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)
    categorizes = models.CharField(max_length=100)
    notes = models.CharField(max_length=150)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.title,self.notes