from rest_framework import serializers
from message_sender.models import Message


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
