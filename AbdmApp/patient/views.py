from django.http import HttpResponse
from .models import Doctor,Patient
from django.http import Http404
from rest_framework import viewsets
from django_filters import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import *
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes,authentication_classes,parser_classes
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser


class PatientList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,  *args, **kwargs):
        snippets = Patient.objects.all()
        serializer = Patientserializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request,  *args, **kwargs):
        serializer = Patientserializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PatientDetails(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Patientserializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Patientserializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
