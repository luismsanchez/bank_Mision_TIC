from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PQR, PersonaSoporte, Bank

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'

class PersonaSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'


class PQRSerializer(serializers.ModelSerializer):
    persona_soporte = PersonaSoporteSerializer(read_only=True)
    class Meta:
        model = PQR
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Bank
        fields = ['users', 'name']