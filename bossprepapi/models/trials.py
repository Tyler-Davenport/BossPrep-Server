from django.db import models
from .users import User

class Trial(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
    User,
        to_field='firebaseKey',
        on_delete=models.CASCADE,
        related_name='trials'
    )
