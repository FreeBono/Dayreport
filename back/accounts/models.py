from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass
    # def __str__(self):  
    #     return f'{self.pk}'
    # excercise = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="workers", null=True)

