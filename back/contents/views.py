from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import WorkoutSerializer
from .models import Workout
from accounts.models import User
from django.shortcuts import get_object_or_404
# Create your views here.



@api_view(['POST'])
@permission_classes([AllowAny])
def Workoutinfo(request):
    if request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data)
 
        user = User.objects.filter(username=request.data.get('userr')).first()
    
        # return Response(request.data2)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            
            return Response(serializer.data)
        # return Response(request.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def Calendar(request):
    if request.method == 'POST':
        workout = Workout.objects.all()
        serializer = WorkoutSerializer(workout,many=True,)
        print(serializer)
        return Response(serializer.data)