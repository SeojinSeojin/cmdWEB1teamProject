from django.db import models
from datetime import timezone
from users import models as user_models


class Wiki(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    update_date = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
