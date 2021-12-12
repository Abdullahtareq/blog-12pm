from django.db import models

# Create your models here.
class Post(models.Model):

    STATS = ( 
        (0, "Draft")
        (1, "Published")
    )

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(null=True, blank=True)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATS, default=0)