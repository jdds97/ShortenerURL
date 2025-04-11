from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import URLShortenerSerializer
from .models import URL
from urllib.parse import urlparse

# Create your views here.
class URLShortenerView(viewsets.ModelViewSet):
    queryset= URL.objects.all()
    serializer_class = URLShortenerSerializer

    @staticmethod
    def is_valid_url(url):
            try:
                result = urlparse(url)
                return all([result.scheme, result.netloc])
            except:
                return False

    def create(self, request, *args, **kwargs):
        # Validate URL
        if not request.data.get('url') or not isinstance(request.data.get('url'), str):
            return Response({"error": "URL is required"}, status=400)
        instance = super().create(request, *args, **kwargs)
        

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Check if URL is valid
        url = request.data.get('url')

        if not URLShortenerView.is_valid_url(url):
            return Response({"error": "Invalid URL format"}, status=400)
            
        self.perform_create(serializer)
        instance = serializer.instance
        instance.accessCount = 0
        instance.save()
        return Response(serializer.data, status=201)
    
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset(), shortCode=kwargs['pk'])
        instance.accessCount += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)
