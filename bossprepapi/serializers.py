from rest_framework import serializers
from bossprepapi.models.trial_questions import TrialQuestion
from bossprepapi.models.users import User
from bossprepapi.models.questions import Question
from bossprepapi.models.responses import Response
from bossprepapi.models.trials import Trial


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'firebaseKey', 'name', 'displayName', 'email']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'job_role', 'job_field', 'created_by']

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'trial', 'question', 'user', 'trial_question', 'response_text', 'created_at']

class TrialQuestionSerializer(serializers.ModelSerializer):
    trial = serializers.PrimaryKeyRelatedField(queryset=Trial.objects.all(), required=False, allow_null=True)
    class Meta:
        model = TrialQuestion
        fields = ['id', 'trial', 'question', 'user']

class TrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trial
        fields = ['id','title', 'created_by']
