from django.db import models
from .trials import Trial
from .questions import Question

class TrialQuestion(models.Model):
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE, related_name='trial_questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='trial_questions')
