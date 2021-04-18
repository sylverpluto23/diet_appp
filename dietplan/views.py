from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from .models import UserInfoModel
from .forms import UserInfo

# Create your views here.
def home(request):
    return render(request, 'dietplan/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'dietplan/signupuser.html', {'form': UserCreationForm()})
    else:  # create user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('user_info')
            except IntegrityError:
                return render(request, 'dietplan/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'Username already taken, please choose another user name'})


        else:
            return render(request, 'dietplan/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'passwords did not match'})


def bmi(request):
    return render(request, 'dietplan/bmi.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'dietplan/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'dietplan/loginuser.html',
                          {'form': AuthenticationForm, 'error': 'username and password did not match'})
        else:
            login(request, user)
            return redirect('user_info')

def bmi1(request):
    weight = request.GET['weight']
    height = request.GET['height']
    bmi1 = round(float(weight)/ (float(height)* float(height)))

    return render(request, 'dietplan/bmi1.html', {'bmi1':bmi1})

# def caloriecount(request):
#     # male = request.GET['gender']
#     # female = request.GET['female']
#     # gender2= request.GET['female']
#     # weight = float(request.GET['weight'])
#     # height = float(request.GET['height'])
#     # age = float(request.GET['age'])
#     # # female = request.GET['female']
#     # male = request.GET['male']
#     # activityfactor = request.GET['activity factor']
#     if request.GET['gender'] == 'male':
#         # caloriecount = ( 13.397(weight) + 4.799(height) - 5.677(age) + 88.362)
#         caloriecount = "maleooo"
#     else:
#         # caloriecount = (9.247(weight) + 3.098(height) - 4.330(age) + 447.593)
#         caloriecount = "femaleaaa"
#     return render(request, 'dietplan/caloriecount.html',{'caloriecount':caloriecount})
#
#
# def male(request):
#     weight1 = request.POST['weight1']
#     height1 = request.POST['height1']
#     age1 = request.POST['age1']
#     male = float(weight1) + float(height1) + float(age1)
#     return render(request, 'dietplan/male.html', {'male':male})
# def p1(request):
#     return render(request, 'dietplan/p1.html',)

def p1(request):
    return render(request,'dietplan/p1.html')

def p2(request):
    return render(request,'dietplan/p2.html' )

def p3(request):
    return render(request,'dietplan/p3.html' )

def p4(request):
    return render(request,'dietplan/p4.html' )

def p5(request):
    return render(request,'dietplan/p5.html' )

def p6(request):
    return render(request,'dietplan/p6.html' )

def p7(request):
    return render(request,'dietplan/p7.html' )

def p8(request):
    return render(request,'dietplan/p8.html' )

def p9(request):
    return render(request,'dietplan/p9.html' )

def p10(request):
    return render(request,'dietplan/p10.html' )

def p11(request):
    return render(request,'dietplan/p11.html' )

def p12(request):
    return render(request,'dietplan/p11.html' )


def p13(request):
    return render(request,'dietplan/p13.html' )

def p14(request):
    return render(request,'dietplan/p14.html' )

def p15(request):
    return render(request,'dietplan/p15.html' )

def p16(request):
    return render(request,'dietplan/p16.html' )

def p17(request):
    return render(request,'dietplan/p17.html' )

def p18(request):
    return render(request,'dietplan/p18.html' )

def p19(request):
    return render(request,'dietplan/p19.html' )

def user_info(request):
    context_dict = {''}
    form = UserInfo()
    list = UserInfoModel.objects.all()
    age = 0
    height=0
    weight = 0
    gender_choice = 'male'
    bmr = 0
    activity_choices = 'no'
    mild_weightloss = 0
    weight_loss = 0
    extreme_weightloss = 0
    breakfast = 'breakfast'
    snack1 = 'snack1'
    lunch =  'lunch'
    snack2 = 'snack'
    dinner = 'dinner'
    if request.method == 'POST':
        form = UserInfo(request.POST)
        if form.is_valid():
            form.save(commit=True)
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender_choice = form.cleaned_data['gender_choice']
            activity_choices = form.cleaned_data['activity_choices']
            if gender_choice == 'male':
                bmr = 13.397*weight + 4.799*height - 5.677*age + 88.362
            else:
                bmr = 9.247*weight + 3.098*height - 4.330*age + 447.593
            if activity_choices == 'no':
                bmr = round(bmr*1.2)
            elif activity_choices == 'little':
                bmr = round(bmr*1.375)
            elif activity_choices == 'moderate':
                bmr = round(bmr*1.55)
            elif activity_choices == 'heavy':
                bmr= round(bmr*1.725)
            else:
                bmr= round(bmr*1.9)
            # mild_weightloss = bmr - 250
            # weight_loss = bmr - 500
            # extreme_weightloss = bmr - 1000
            if 800<bmr<900  :
                # breakfast = 'Breakfast: All bran cereal, 1 cup milk , 1 banana'
                # snack1 = 'Snack :Cucumber ,Avocado dip'
                # lunch = 'Lunch: Grilled cheese with tomato ,Salad'
                # snack2 = 'Snack: walnuts'
                # dinner = 'Dinner: Grilled Chicken ,Brussel sprouts , Quinoa'
                return redirect('p1')
            elif 900<bmr<1000:
                return redirect('p2')
            elif 1000<bmr<1100:
                return redirect('p3')
            elif 1100<bmr<1200:
                return redirect('p4')
            elif 1200<bmr<1300:
                return redirect('p5')
            elif 1300<bmr<1400:
                return redirect('p6')
            elif 1400<bmr<1500:
                return redirect('p7')
            elif 1500<bmr<1600:
                return redirect('p8')
            elif 1600<bmr<1700:
                return redirect('p9')
            elif 1700<bmr<1800:
                return redirect('p10')
            elif 1800<bmr<1900:
                return redirect('p11')
            elif 1900<bmr<2000:
                return redirect('p12')
            elif 2000<bmr<2100:
                return redirect('p13')
            elif 2100<bmr<2200:
                return redirect('p14')
            elif 2200<bmr<2300:
                return redirect('p15')
            elif 2300<bmr<2400:
                return redirect('p16')
            elif 2400<bmr<2500:
                return redirect('p17')
            elif 2500<bmr<2600:
                return redirect('p18')
            else:
                return redirect('p19')














            # print("Name" + form.cleaned_data['name'])
            # print("Gender" , form.cleaned_data['gender_choice'])
            # print("height" , form.cleaned_data['height'])
            # print("weight", form.cleaned_data['weight'])
            # print("age" , form.cleaned_data['age'])
        else:
            print('error')
    return render(request, 'dietplan/user_info.html', {'form':form , 'list':list,'age':age , 'height':height, 'weight':weight, 'gender_choice':gender_choice , 'bmr':bmr, 'activity_choices':activity_choices, 'mild_weightloss':mild_weightloss, 'weight_loss':weight_loss, 'extreme_weightloss':extreme_weightloss, 'breakfast':breakfast, 'snack1':snack1,  'lunch':lunch, 'snack2':snack2, 'dinner':dinner ,} )

