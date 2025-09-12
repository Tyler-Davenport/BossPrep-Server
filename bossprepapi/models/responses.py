
from django.db import models
from .trials import Trial
from .questions import Question
from .users import User

class Response(models.Model):
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses')
    user = models.ForeignKey(User, to_field='firebaseKey', on_delete=models.CASCADE, related_name='responses')
    trial_question = models.ForeignKey('bossprepapi.TrialQuestion', on_delete=models.CASCADE, related_name='responses', null=True, blank=True)
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
