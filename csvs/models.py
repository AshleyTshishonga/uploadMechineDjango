from django.db import models
from django.contrib.auth.models import User,auth
from distutils.command.upload import upload
# Create your models here.


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"