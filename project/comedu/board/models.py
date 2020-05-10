from django.db import models
from django.utils import timezone
from users import models as user_models

# Create your models here.


class Post(models.Model):
    # User관리는 조금더 공부 후에 추가할 예정
    #writer = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    genre_choices = [
        ("C", "C"),
        ("C++", "C++"),
        ("Python", "Python"),
        ("Javacript", "Javascript"),
        ("R", "R"),
        ("Others", "Others"),
        ("Text", "Text")
    ]

    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    genre = models.CharField(max_length=10, choices=genre_choices)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def onlyMonthDay(self):
        month = self.pub_date.strftime("%m")
        day = self.pub_date.strftime("%d")
        monthDay = str(month) + "/" + str(day)
        return monthDay
    onlyMonthDay.short_description = "pub month/day"
