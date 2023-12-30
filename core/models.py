from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    def __str__(self) -> str:
        return self.name
    
