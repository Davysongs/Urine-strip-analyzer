from django.urls import path
from .views import ImageUploadView, upload_image_view


urlpatterns = [
    path('', upload_image_view, name='upload_image'),
    path('api/upload/', ImageUploadView.as_view(), name='image-upload'),
]
