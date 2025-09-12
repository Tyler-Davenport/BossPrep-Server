from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bossprepapi.models.trial_questions import TrialQuestion
from bossprepapi.serializers import TrialQuestionSerializer

class TrialQuestionViewSet(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            trial_question = TrialQuestion.objects.get(pk=pk)
            serializer = TrialQuestionSerializer(trial_question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TrialQuestion.DoesNotExist:
            return Response({'error': 'TrialQuestion not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        trial_id = request.query_params.get('trial')
        user = request.query_params.get('user')
        if trial_id:
            trial_questions = TrialQuestion.objects.filter(trial=trial_id)
        elif user:
            trial_questions = TrialQuestion.objects.filter(user=user)
        else:
            return Response({'error': 'trial or user required as query param'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TrialQuestionSerializer(trial_questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TrialQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            trial_question = TrialQuestion.objects.get(pk=pk)
            trial_id = request.data.get('trial')
            # Allow trial to be set to None (null)
            trial_question.trial_id = trial_id if trial_id is not None else None
            question_id = request.data.get('question')
            user_id = request.data.get('user')
            if question_id is not None:
                trial_question.question_id = question_id
            if user_id is not None:
                trial_question.user_id = user_id
            trial_question.save()
            serializer = TrialQuestionSerializer(trial_question)
            return Response(serializer.data)
        except TrialQuestion.DoesNotExist:
            return Response({'error': 'TrialQuestion not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            trial_question = TrialQuestion.objects.get(pk=pk)
            trial_question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TrialQuestion.DoesNotExist:
            return Response(
                {"error": "Saved question not found"}, status=status.HTTP_404_NOT_FOUND
            )
