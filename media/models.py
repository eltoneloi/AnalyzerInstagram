from django.db import models

# Create your models here.

class Media(models.Model):
    creator=models.CharField(max_length = 100)
    media_id = models.IntegerField()
    
    def __str__(self):
        return self.name
    