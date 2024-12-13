from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
