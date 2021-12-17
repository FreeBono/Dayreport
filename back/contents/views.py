from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import WorkoutSerializer
from .models import Workout
from accounts.models import User
from django.shortcuts import get_object_or_404
import json
# Create your views here.



@api_view(['POST'])
@permission_classes([AllowAny])
def Workoutinfo(request):
    if request.method == 'POST':
        print(request.data)
        serializer = WorkoutSerializer(data=request.data)
        workset = json.dumps(request.data['set'])
        worktime = json.dumps(request.data['time'])
        user = User.objects.filter(username=request.data.get('userr')).first()
        print(serializer)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, se=workset, tim = worktime)
            
            return Response(serializer.data)
        # return Response(request.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def Calendar(request):
    if request.method == 'POST':
        workout = Workout.objects.all()
        serializer = WorkoutSerializer(workout,many=True,)
        # print(serializer)
        return Response(serializer.data)