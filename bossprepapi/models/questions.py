from django.db import models
from .users import User

class Question(models.Model):
    question_text = models.TextField()
    job_field = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    created_by = models.ForeignKey(
    User,
        to_field='firebaseKey',
        on_delete=models.CASCADE,
        related_name='questions'
    )
