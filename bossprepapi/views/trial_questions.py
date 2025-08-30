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
        user = request.query_params.get('user')
        if not user:
            return Response({'error': 'user required as query param'}, status=status.HTTP_400_BAD_REQUEST)
        trial_questions = TrialQuestion.objects.filter(user=user)
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
            if trial_id is not None:
                trial_question.trial_id = trial_id
                trial_question.save()
                serializer = TrialQuestionSerializer(trial_question)
                return Response(serializer.data)
            return Response({'error': 'trial id required'}, status=status.HTTP_400_BAD_REQUEST)
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
