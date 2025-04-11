from rest_framework import serializers
from .models import URL

class URLShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id','url', 'shortCode', 'created_at', 'updated_at', 'accessCount']
        read_only_fields = ['id','shortCode', 'created_at', 'updated_at', 'accessCount']