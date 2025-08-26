from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bossprepapi.models.responses import Response
from bossprepapi.serializers import ResponseSerializer

class ResponseViewSet(ViewSet):
    def create(self, request):
        return Response({"message": "Response created"}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, question_id):
        responses = Response.objects.filter(question_id=question_id)
        serializer = ResponseSerializer(responses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        return Response({"message": "List of responses"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({"message": f"Response {pk} deleted"}, status=status.HTTP_204_NO_CONTENT)
