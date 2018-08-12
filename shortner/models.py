from django.db import models
#The Database Model is created.
# Create your models here.
class Shortify(models.Model):
    longURL=models.CharField(max_length=900)
    addDate = models.DateTimeField(auto_now_add=True)
    autoIncrement = models.AutoField(primary_key=True)
    shortURL=models.CharField(max_length=600)
    clickCount=models.CharField(max_length=1000)

