from rest_framework import serializers
from .models import Workout
from accounts.serializers import UserSerializer

class WorkoutSerializer(serializers.ModelSerializer):
    addd = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = '__all__'

