"""diet_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dietplan import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    # logout
    path('logout/', views.logoutuser, name='logoutuser'),
    # loginpage
    path('login/', views.loginuser, name='loginuser'),
    #after loging in it'll send them to this page
    path('bmi/', views.bmi , name='bmi' ),
    #after pressing submit on bmi page
    # path('bmi/bmiresult', views.bmiresult, name='bmiresult')
    path('bmi/bmi1', views.bmi1 ,name='bmi1'),
    # # #caloriecounting
    # path('caloriecount/', views.caloriecount ,name='caloriecount'),
    # path('male/', views.male, name='male')
    path('user_info/', views.user_info , name='user_info'),
path('p1/', views.p1 , name='p1'),
path('p2/', views.p2 , name='p2'),
path('p3/', views.p3 , name='p3'),
path('p4/', views.p4 , name='p4'),
path('p5/', views.p5 , name='p5'),
path('p6/', views.p6, name='p6'),
path('p7/', views.p7 , name='p7'),
path('p8/', views.p8, name='p8'),
path('p9/', views.p9 , name='p9'),
path('p10/', views.p10 , name='p10'),
path('p11/', views.p11 , name='p11'),
path('p12/', views.p12 , name='p12'),
path('p13/', views.p13 , name='p13'),
path('p14/', views.p14 , name='p14'),
path('p15/', views.p15 , name='p15'),
path('p16/', views.p16 , name='p16'),
path('p17/', views.p17 , name='p17'),
path('p18/', views.p18 , name='p18'),
path('p19/', views.p19 , name='p19'),

]
