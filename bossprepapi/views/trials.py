from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bossprepapi.models.trials import Trial
from bossprepapi.serializers import TrialSerializer

class TrialViewSet(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            trial = Trial.objects.get(pk=pk)
            serializer = TrialSerializer(trial)
            return Response(serializer.data)
        except Trial.DoesNotExist:
            return Response({'error': 'Trial not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        created_by = request.query_params.get('created_by')
        if created_by:
            trials = Trial.objects.filter(created_by=created_by)
        else:
            trials = Trial.objects.all()
        serializer = TrialSerializer(trials, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TrialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            trial = Trial.objects.get(pk=pk)
            serializer = TrialSerializer(trial, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Trial.DoesNotExist:
            return Response({'error': 'Trial not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            trial = Trial.objects.get(pk=pk)
            trial.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Trial.DoesNotExist:
            return Response({'error': 'Trial not found'}, status=status.HTTP_404_NOT_FOUND)
