from django.db import models

# from accounts.models import User
from django.conf import settings
# Create your models here.
# workout_choices = ('deadlift','deadlift'),('barbellrow','barbellrow'),('dumbellrow','dumbellrow'),('seatedrow','seatedrow'),('pullup','pullup'),
# ('letpulldown','letpulldown'),('cablepulldown','cablepulldown'),('benchpress','benchpress'),('inclinebenchpress','inclinebenchpress'),
# ('dips','dips'),('chestpress','chestpress'),('dumbellbenchpress','dumbellbenchpress'),('cablepushdown','cablepushdown'),('overheadpress','overheadpress'),('dumbellshoulderpress','dumbellshoulderpress'),('militarypress','militarypress'),('lateralpress','lateralpress'),('frontraise','frontraise'),
# ('shoulderpress','frontraise'),('squat','squat'),('lunge','lunge'),('legpress','legpress'),('legextension','legextension'),('legcurl','legcurl'),('innerthigh','innerthigh' )
class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="workout", null=True)
    workoutlist = models.CharField(max_length=200, null=True)
    se = models.TextField(null=True)
    tim = models.TextField(null=True)
    settotal = models.IntegerField(null=True) 
    timetotal = models.IntegerField(null=True) 

    def __str__(self):
        return f'{self.user}'    
    # deadlift = models.IntegerField(null=True)
    # deadlift2 = models.IntegerField(null=True)
    # barbellrow = models.IntegerField(null=True)
    # barbellrow2 = models.IntegerField(null=True)
    # dumbellrow = models.IntegerField(null=True)
    # dumbellrow2 = models.IntegerField(null=True)
    # seatedrow = models.IntegerField(null=True)
    # seatedrow2 = models.IntegerField(null=True)
    # pullup = models.IntegerField(null=True)
    # pullup2 = models.IntegerField(null=True)
    # letpulldown = models.IntegerField(null=True)
    # letpulldown2 = models.IntegerField(null=True)
    # cablepulldown = models.IntegerField(null=True)
    # cablepulldown2 = models.IntegerField(null=True)
    # benchpress = models.IntegerField(null=True)
    # benchpress2 = models.IntegerField(null=True)
    # inclinebenchpress = models.IntegerField(null=True)
    # inclinebenchpress2 = models.IntegerField(null=True)
    # dips = models.IntegerField(null=True)
    # dips2 = models.IntegerField(null=True)
    # chestpress = models.IntegerField(null=True)
    # chestpress2 = models.IntegerField(null=True)
    # dumbellbenchpress = models.IntegerField(null=True)
    # dumbellbenchpress2 = models.IntegerField(null=True)
    # cablepushdown = models.IntegerField(null=True)
    # cablepushdown2 = models.IntegerField(null=True)
    # overheadpress = models.IntegerField(null=True)
    # overheadpress2 = models.IntegerField(null=True)
    # dumbellshoulderpress = models.IntegerField(null=True)
    # dumbellshoulderpress2 = models.IntegerField(null=True)
    # militarypress = models.IntegerField(null=True)
    # militarypress2 = models.IntegerField(null=True)
    # lateralpress = models.IntegerField(null=True)
    # lateralpress2 = models.IntegerField(null=True)
    # frontraise = models.IntegerField(null=True)
    # frontraise2 = models.IntegerField(null=True)
    # shoulderpress = models.IntegerField(null=True)
    # shoulderpress2 = models.IntegerField(null=True)
    # squat = models.IntegerField(null=True)
    # squat2 = models.IntegerField(null=True)
    # lunge =models.IntegerField(null=True)
    # lunge2 =models.IntegerField(null=True)
    # legpress = models.IntegerField(null=True)
    # legpress2 = models.IntegerField(null=True)
    # legextension = models.IntegerField(null=True)
    # legextension2 = models.IntegerField(null=True)
    # legcurl = models.IntegerField(null=True)
    # legcurl2 = models.IntegerField(null=True)
    # innerthigh =models.IntegerField(null=True)
    # innerthigh2 =models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # deadlift = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="deadlifts")
    # barbellrow = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="barbellrows")
    # dumbellrow = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="dumbellrows")
    # seatedrow = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="seatedrows")
    # pullup = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="pullups")
    # letpulldown = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="letpulldowns")
    # cablepulldown = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="cablepulldowns")
    # benchpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="benchpresss")
    # inclinebenchpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="inclinebenchpresss")
    # dips = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="dipss")
    # chestpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="chestpresss")
    # dumbellbenchpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="dumbellbenchpresss")
    # cablepushdown = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="cablepushdowns")
    # overheadpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="overheadpresss")
    # dumbellshoulderpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="dumbellshoulderpresss")
    # militarypress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="militarypresss")
    # lateralpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="lateralpresss")
    # frontraise = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="frontraises")
    # shoulderpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="shoulderpresss")
    # squat = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="squats")
    # lunge = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="lunges")
    # legpress = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="legpresss")
    # legextension = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="legextensions")
    # legcurl = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="legcurls")
    # innerthigh = models.ForeignKey(Workoutinfo, on_delete=models.CASCADE, related_name="innerthighs")


