from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from .serializers import *
from .models import *


class ClientsLists(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        clients = Clients.objects.all()
        serializer = ClientsSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, id):
        try:
            return Clients.objects.get(pk=id)
        except Clients.DoesNotExist:
            raise Http404

    def get(self, request, id):
        client = self.get_object(id)
        serializer = ClientsSerializer(client)
        return Response(serializer.data)

    def put(self, request, id):
        client = self.get_object(id)
        serializer = ClientsSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        client = self.get_object(id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostsListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class EmployListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Employees.objects.all()
    serializer_class = EmployeesListSerializer


class EmployDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Employees.objects.all()
    serializer_class = EmployeesDetailSerializer
