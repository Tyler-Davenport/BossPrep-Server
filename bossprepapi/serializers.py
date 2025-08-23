from rest_framework import serializers
from bossprepapi.models.users import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'firebaseKey', 'name', 'displayName', 'email']
