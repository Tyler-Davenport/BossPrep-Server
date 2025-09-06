
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bossprepapi.models.users import User
from bossprepapi.serializers import UserSerializer

class UserView(APIView):
	def get(self, request, uid=None):
		if uid is None:
			users = User.objects.all()
			serializer = UserSerializer(users, many=True)
			return Response(serializer.data)
		try:
			user = User.objects.get(uid=uid)
			serializer = UserSerializer(user)
			return Response(serializer.data)
		except User.DoesNotExist:
			return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			if User.objects.filter(uid=serializer.validated_data['uid']).exists():
				return Response({'error': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, uid=None):
		if uid is None:
			return Response({'error': 'UID required.'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			user = User.objects.get(uid=uid)
			user.delete()
			return Response({'success': f'User {uid} deleted.'}, status=status.HTTP_204_NO_CONTENT)
		except User.DoesNotExist:
			return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
