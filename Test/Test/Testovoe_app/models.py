from django.db import models
from django.forms import DateTimeField


class database(models.Model):
    title = models.CharField(max_length=255, verbose_name=("Криптоволюты"))
    content = models.TextField(blank = True)
    photo = models.ImageField(upload_to="photos/")
    time_update = models.DateTimeField(auto_now = True)
    is_pub = models.BooleanField(default=True)
    # def get_absolut_url(self):
    #     return reverse("post")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Криптоволюты"
        verbose_name_plural = "Крипта"
        ordering = ["title"]