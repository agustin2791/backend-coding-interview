from rest_framework import serializers
from .models import Photo

# Serialize Photo model with all the fields
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'