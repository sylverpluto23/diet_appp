from django.db import models



#setting aruguments for widgets
male = 'male'
female = 'female'
no = 'no'
little = 'little'
moderate = 'moderate'
heavy = 'heavy'
veryheavy = 'veryheavy'
GENDER_CHOICE = [('male', 'Male'), ('female','Female'),]
# ACTIVITY_FACTOR_CHOICE = []
ACTIVITY_CHOICES = [('no', 'Little or no exercise'), ('little', 'Exercise 1-3 days a Week'),('moderate', 'Exercise, 3-5 days a week'),('heavy', 'Heavy Exercise, 6-7 days a week'), ('veryheavy', 'Very heavy Exercise, twice per day') ]

# Create your models here.
class UserInfoModel(models.Model):
    name = models.CharField(max_length=20)
    gender_choice = models.CharField(max_length=6 , choices=GENDER_CHOICE,)
    height_in_cm = models.FloatField()
    weight_in_kg = models.FloatField()
    age = models.FloatField()
    activity_choices = models.CharField(max_length=150, default= 'NULL' ,  choices=ACTIVITY_CHOICES,)

    def __str__(self):
        return self.name 
