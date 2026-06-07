from django.db import models

# Create your models here.
class CyberTweets(models.Model):
    tweets=models.TextField()
    cyber_data=models.CharField(max_length=500)