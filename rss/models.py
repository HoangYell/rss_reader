from django.db import models


class Rss(models.Model):
    title = models.CharField(max_length=60)
    link = models.CharField(max_length=120)
    description= models.TextField()
    author = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    enclosure = models.CharField(max_length=120)
    comments = models.CharField(max_length=120)
    pub_date = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=120)
