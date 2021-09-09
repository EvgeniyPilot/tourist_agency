from .models import *
from rest_framework import serializers


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'name', 'address']


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class EmployeesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class EmployeesDetailSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field="namepost", read_only=True)

    class Meta:
        model = Employees
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = AuthUser.objects.create()
        user.set_password(validated_data['password'])
        user.save()
        return user
