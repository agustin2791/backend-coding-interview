from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Photo
from .serializers import PhotoSerializer
# Create your views here.
class PhotoListView(APIView):
    '''
    API Endpoint to get a list of photos or to create a new photo
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.auth)
        all_photos = Photo.objects.all()
        serializer = PhotoSerializer(all_photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class PhotoDetailsView(APIView):
    '''
    API endpoint to get, update, delete a specific photo
    '''
    permission_classes = [IsAuthenticated]
    www_authenticate_realm = 'api'

    def get(self, request, photo_id, format=None):
        '''GET the details of a specific photo in the database based on the photo id (photo_id)'''
        try:
            photo = Photo.objects.get(id=photo_id)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Photo.DoesNotExist:
            return Response({'error': 'Photo does not exists'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, photo_id):
        '''UPDATE the details of specific photo in the database based on the photo id (photo_id)'''
        try:
            photo = Photo.objects.get(id=photo_id)
        except Photo.DoesNotExist:
            return Response({'error': 'Photo does not exists'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, photo_id):
        '''DELETE a photo on the database based on photo id (photo_id)'''
        try:
            photo = Photo.objects.get(id=photo_id)
            photo.delete()
        except Photo.DoesNotExist:
            return Response({'error': 'Photo does not exists'}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "One Item deleted"}, status=status.HTTP_200_OK)