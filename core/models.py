from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=43)
    body = models.TextField()

    def __str__(self):
        return self.name
    
