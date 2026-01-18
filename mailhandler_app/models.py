from django.db import models


# Create your models here.
class Mailhandler(models.Model):
    subject=models.CharField(max_length=100)
    message=models.TextField()
    recipient_list=models.JSONField()
    sent_at=models.TimeField(auto_now_add=True)
    sent_count=models.IntegerField(default=0)


def __str__(self):
        return f"{self.subject} - {self.sent_at}"