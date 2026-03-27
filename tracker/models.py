from django.db import models


class StudySession(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.title
