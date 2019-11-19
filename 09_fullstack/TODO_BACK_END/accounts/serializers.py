from rest_framework import serializers
from django.contrib.auth import get_user_model

from todos.serializers import TodoSerializer
User = get_user_model()

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class UserSerializer(serializers.ModelSerializer):
    # 사용자 1명에 대한 serial이지만, 해당유저의 Todos를 모두 포함!
    todo_set = TodoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set',)