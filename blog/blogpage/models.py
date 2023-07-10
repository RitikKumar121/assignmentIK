from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now


class BlogPostTable(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=14)
    timeStamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title + " by "+self.author
