from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('home/',views.index, name = "home"),
    path('register/',views.register, name = "register"),
    path('login/',views.login, name ='login'),
    path('dashboard/',views.dashboard, name ="dashboard"),
    path('logout/',views.logout, name='logout'),
    path('main/',views.main, name="main"),
    path('attendence/',views.attendence, name ='attendence'),
    path('profile/',views.profile, name='profile'),
    path('feedback/',views.feedback1, name='feedback'),
    path('aboutUs/',views.aboutus , name = 'aboutus'),
    path('feed/',views.feed, name = 'homefeed'),
    path('notifications/',views.notifications, name='notifications'),
    path('project/',views.project, name = "project"),
    path('admin/',views.adminhome, name = 'admin'),
    path('adminlogin/',views.adminlogin,name = 'adminlogin'),
    path('admindash/',views.admindashboard,name='admindash'),
    path('adminlogout/',views.adminlogout, name='adminlogout'),
    path('adminproject/',views.adminproject,name='adminproject'),
    path('adminprofile/',views.adminprofile, name='adminprofile'),
    path('projectdetail/',views.projectdetail,name='projectdetail'),
    path('delete/<int:id>',views.delete),
    path('adminfeedback/',views.adminfeedback, name='adminfeedback'),
    path('deletefeed/<int:id>',views.deletefeed),
    path('deleteemp/<int:id>',views.deleteemp),
   
]
