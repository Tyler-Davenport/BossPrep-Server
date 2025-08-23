from django.db import models

class Users(models.Model):
    firebaseKey = models.CharField(max_length=255, primary_key=True)
    uid = models.IntegerField()
    name = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
