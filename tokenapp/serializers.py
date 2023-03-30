from rest_framework import serializers

from .models import Token

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
        depth = 3



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
        depth = 3
