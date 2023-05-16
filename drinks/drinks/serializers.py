from rest_framework import serializers
from .models import Drikns
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drikns
        fields = '__all__'