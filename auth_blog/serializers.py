from rest_framework import serializers
from .models import auth_blog

class auth_blogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'genre', 'description', 'created_at')
        model = auth_blog 