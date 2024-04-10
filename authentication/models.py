from django.db import models
from django.utils import timezone

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length = 50)
    email    = models.EmailField()
    password = models.CharField(max_length = 50)
    datetime = models.DateField(default = timezone.now)
    

    def __str__(self):
        return self.username
    