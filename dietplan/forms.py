from django import forms
from .models import UserInfoModel

#setting aruguments for widgets
GENDER_CHOICE = [('male', 'Male'), ('female','Female'),]
ACTIVITY_CHOICES = [('no', 'Little or no exercise'), ('little', 'Exercise 1-3 days a Week'),('moderate', 'Exercise, 3-5 days a week'),('heavy', 'Heavy Exercise, 6-7 days a week'), ('veryheavy', 'Very heavy Exercise, twice per day') ]
class UserInfo(forms.ModelForm):
    class Meta():
        model = UserInfoModel
        fields = '__all__'

