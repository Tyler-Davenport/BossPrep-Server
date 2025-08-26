from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from bossprepapi.models.questions import Question
from bossprepapi.serializers import QuestionSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class QuestionViewSet(ViewSet):
    def list(self, request):
        questions = Question.objects.all()
        job_role = request.query_params.get('job_role')
        job_field = request.query_params.get('job_field')
        if job_role:
            questions = questions.filter(job_role=job_role)
        if job_field:
            questions = questions.filter(job_field=job_field)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            question = Question.objects.get(pk=pk)
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)
