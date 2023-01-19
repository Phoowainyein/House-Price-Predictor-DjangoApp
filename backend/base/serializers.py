from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'is_admin', 'username', 'email', 'name']

    @staticmethod
    def get__id(obj):
        return obj.id

    @staticmethod
    def get_is_admin(obj):
        return obj.is_staff

    @staticmethod
    def get_name(obj):
        print(obj)
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'is_admin', 'username', 'email', 'name', 'token']

    @staticmethod
    def get_token(obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
