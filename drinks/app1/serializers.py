from rest_framework import serializers 
from .models import drinks

class DrinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = drinks
        fields = ['id', 'name', 'description']