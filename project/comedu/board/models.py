from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    # User관리는 조금더 공부 후에 추가할 예정
    #writer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def onlyMonthDay(self):
        month = self.pub_date.strftime("%m")
        day = self.pub_date.strftime("%d")
        monthDay = str(month) + "/" + str(day)
        return monthDay
