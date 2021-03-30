from django.shortcuts import render
from auth_blog.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import auth_blogSerializer
from .models import auth_blog



class auth_blogList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = auth_blog.objects.all()
    serializer_class = auth_blogSerializer

class auth_blogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = auth_blog.objects.all()
    serializer_class = auth_blogSerializer


