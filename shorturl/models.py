from django.db import models

# Create your models here.
class UrlModel(models.Model):
    key_url=models.CharField(max_length=50)
    value_url=models.CharField(max_length=50)
