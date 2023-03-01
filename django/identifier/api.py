from .models import animalIdentifier
from .serializers import AnimalSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status


class ImageList(generics.ListAPIView):
    queryset = animalIdentifier.objects.all().order_by('-uploaded')
    serializer_class = AnimalSerializer


class CreateImage(generics.CreateAPIView):
    serializer_class = AnimalSerializer

    def post(self, request, format=None):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetImageById(APIView):
    def get(self, request, *args, **kwargs):
        image_id = kwargs.get('image_id')
        image_obj = animalIdentifier.objects.get(id=image_id)
        serializer = AnimalSerializer(image_obj)
        return Response(serializer.data)


class ImageDelete(generics.DestroyAPIView):
    queryset = animalIdentifier.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'id'


