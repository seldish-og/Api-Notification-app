from rest_framework import status
from rest_framework.response import Response

from message_sender.models import Message
from .serializers import StatisticSerializer

from django.http import Http404
from rest_framework.views import APIView


class StatisticsView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = StatisticSerializer(messages, many=True)

        return Response(serializer.data)
