from django.db import models
from .trials import Trial
from .questions import Question
from .users import User

class TrialQuestion(models.Model):
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE, related_name='trial_questions', null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='trial_questions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trial_questions')
