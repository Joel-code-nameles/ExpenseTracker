from django.db import models

# Create your models here.
class TrackerApp(models.Model):
    expenses = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=100)

    # the string entries
    def __str__(self):
        return self.expenses