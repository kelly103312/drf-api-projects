from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer
