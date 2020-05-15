from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):

    email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    # FIXME : studentID는 unique한데, superuser 또한 이 model에 들어가므로
    # 두번째 superuser 만들때 studentID 중복문제 발생(공백으로)
    studentID = models.CharField(max_length=10, unique = True)

    avatar = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.studentID} | {self.username}"