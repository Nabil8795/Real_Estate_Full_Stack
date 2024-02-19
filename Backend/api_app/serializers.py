from rest_framework import serializers
from api_app.models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['name', 'price', 'detail', 'image']
