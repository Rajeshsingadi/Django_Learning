from django.db import models

# Create your models here.


class Something(models.Model):
    title = models.CharField(max_length=10)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.rating})"
