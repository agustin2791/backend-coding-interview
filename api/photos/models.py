from django.db import models

# Create your models here.
class Photo(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    url = models.CharField(max_length=255)
    photographer = models.CharField(max_length=255)
    photographer_url = models.CharField(max_length=255)
    photographer_id = models.IntegerField()
    avg_color = models.CharField(max_length=255)
    original = models.CharField(max_length=255)
    large2x = models.CharField(max_length=255)
    large = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    small = models.CharField(max_length=255)
    portrait = models.CharField(max_length=255)
    landscape = models.CharField(max_length=255)
    tiny = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)