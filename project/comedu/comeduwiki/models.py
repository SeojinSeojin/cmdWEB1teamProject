from django.db import models
from datetime import timezone

class Wiki(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Create your models here.
