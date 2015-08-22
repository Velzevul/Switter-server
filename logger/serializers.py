from rest_framework import serializers
from .models import Log, Journal


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
