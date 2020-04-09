from django.db import models

class Article(models.Model):
    Title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(blank=False, default=True)
