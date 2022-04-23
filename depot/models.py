from django.db import models
from datetime import datetime

class User(models.Model):

    username = models.CharField(max_length = 32, unique=True)
    password = models.CharField(max_length = 32)
    doc = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name