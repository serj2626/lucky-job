from rest_framework import serializers
from .models import (
    Cookie,
    Offerta,
    Policy,
)


class OffertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offerta
        fields = ["title", "content"]


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ["title", "content"]


class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = ["title", "content"]
