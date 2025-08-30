
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bossprepapi.models.responses import Response as ResponseModel
from bossprepapi.serializers import ResponseSerializer

class ResponseViewSet(ViewSet):
    def create(self, request):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            response = ResponseModel.objects.get(pk=pk)
            serializer = ResponseSerializer(response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ResponseModel.DoesNotExist:
            return Response({"error": "Response not found."}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        question_id = request.query_params.get('question_id')
        if question_id:
            responses = ResponseModel.objects.filter(question_id=question_id)
        else:
            responses = ResponseModel.objects.all()
        serializer = ResponseSerializer(responses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            response = ResponseModel.objects.get(pk=pk)
            response.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ResponseModel.DoesNotExist:
            return Response({"error": f"Response {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
