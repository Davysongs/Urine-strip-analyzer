from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageUploadSerializer
from .utils import process_image  # function to handle image processing
from django.shortcuts import render

def upload_image_view(request):
    return render(request, 'index.html')


class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            colors = process_image(image)
            return Response(colors)
        return Response(serializer.errors, status=400)
