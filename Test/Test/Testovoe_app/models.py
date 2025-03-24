from django.db import models
from django.forms import DateTimeField


class database(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank = True)
    photo = models.ImageField(upload_to="photos/")
    time_update = models.DateTimeField(auto_now = True)
    is_pub = models.BooleanField(default=True)