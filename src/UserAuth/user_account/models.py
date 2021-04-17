from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Secret(models.Model):
    username        = models.ForeignKey(User, on_delete=models.CASCADE)
    message         = models.CharField(max_length=24)
