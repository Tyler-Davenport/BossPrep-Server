from django.db import models
from .users import Users

class Questions(models.Model):
    question_text = models.TextField()
    job_field = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        Users,
        to_field='firebaseKey',
        on_delete=models.CASCADE,
        related_name='questions'
    )
