from cgi import test
from rest_framework import status
from rest_framework.response import Response

from .models import Client, Mailing
from .serializers import ClientSerializer, MailingSerializer

from django.http import Http404
from rest_framework.views import APIView

from message_sender import tasks


class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        client_data = request.data
        serializer = ClientSerializer(data=client_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, client_id):
        client = Client.objects.get(id=client_id)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client_id):
        client = Client.objects.filter(id=client_id)
        if client:
            client.delete()
            return Response()


class MailingView(APIView):
    def get(self, request):
        mailings = Mailing.objects.all()
        serializer = MailingSerializer(mailings, many=True)
        tasks.start_mailing.delay(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        mailing_data = request.data
        serializer = MailingSerializer(data=mailing_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, mailing_id):
        mailing = Mailing.objects.get(id=mailing_id)
        serializer = MailingSerializer(mailing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client_id):
        mailing = Client.objects.filter(id=client_id)
        if mailing:
            mailing.delete()
            return Response()
