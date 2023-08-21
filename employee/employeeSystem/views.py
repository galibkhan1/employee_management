import email
from django.shortcuts import redirect, render , HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from employeeSystem.models import feedback, registration , userattendence,task
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        data = registration(firstname = firstname , lastname = lastname , password = make_password(password), email = email , gender = gender , phone =contact)
        data.save()
    return render (request, 'index.html')

def login(request):
    error_msg = None
    if request.method == "POST":
        emails = request.POST.get('email')
        password = request.POST.get('password')
        try:
            logindata = registration.objects.get(email=emails)
            if logindata:
                request.session['email'] = emails
                request.session['username'] = logindata.firstname 
                request.session['lastname'] = logindata.lastname
                # request.session['la'] = logindata.lastname
                return redirect('dashboard')    
        except:
            error_msg = "invalid email"
            return render(request, 'main.html', {'error_msg': error_msg})

# def login(request):
#     error_msg = None

#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             userdata = registration.objects.get(email = email)
#             if (userdata.email == email):
#                 flag = check_password(password, userdata.password)
#                 if flag:
#                     request.session['email'] = email
#                     request.session['password'] = password
#                     return redirect('dashboard')
#                 else:
#                     error_msg = "Please Enter valid password"
#                     return render(request, 'main.html',{'error_msg': error_msg})
#             return HttpResponseRedirect(userdata.email, userdata.passw)
#         except:
#             error_msg = "Please Enter valid Email"
#             return render(request, 'main.html',{'error_msg':error_msg})

#         return HttpResponse(userdata.email,userdata.password)
# def login(request):
#     error_msg = None
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             userdata = registration.objects.get(email=email)
#             if (userdata.email == email):
#                 flag = check_password(userdata.password , password)
#                 print(flag)
#                 if flag:
#                     request.session['email'] = userdata.email
#                     return redirect('dashboard')
#                 else:
#                     error_msg = "Please Enter valid password"
#                     return render(request, 'main.html', {'error_msg': error_msg})
#         except:
#             error_msg = "Please Enter valid  Email"
#             return render(request, 'main.html', {'error_msg': error_msg})

#         return HttpResponse(userdata.email, userdata.password)
def dashboard(request):
    try:
        c = request.session['email']

        username = registration.objects.filter(email= c)

        return render(request , 'dashboard.html',{'username':username})
    except:
        return redirect('main')

def logout(request):
    request.session.clear()
    return redirect('main')

def main(request):
    return render(request, 'main.html')


def attendence(request):
    c = request.session['email']

    username = registration.objects.filter(email= c)
    return render(request , 'attendence.html',{'username':username})

def profile(request):
    c = request.session['email']

    username = registration.objects.filter(email= c)
    return render(request , 'profile.html',{'username':username})
def feedback1(request):
    c = request.session['username']
    if request.method =="POST":
        feed = request.POST.get('feedback')
        user_feed = feedback(userfeedback = feed,username = c)
        user_feed.save()
    a = feedback.objects.all()
    data= feedback.objects.filter(username = c)
    context = {
        'a':a
    }
    c = request.session['email']
    username = registration.objects.filter(email= c)
    # return render(request , 'feedback.html',{'username':username})
    data = {
        'username':username
    }
    return render(request ,'feedback.html',{'a':a , 'username':username , 'data':data})
def aboutus(request):
    return render(request ,'aboutUs.html')
def feed(request):
    a = feedback.objects.all()
    context = {
        'a':a
    }
    return render(request,'feedback.html',context)
def attendence(request):
    c = request.session['email']
    username = registration.objects.filter(email= c)
    a = request.session['username'] 
    if request.method == "POST":
        atten = request.POST.get('attened')
        request.session['att'] = atten
        attendencedata = userattendence(attendence = atten , username = a)
        attendencedata.save()
    data = {
        'username':username
    }
    return render(request, 'attendence.html',data)

def project(request):
    c = request.session['email']
    data = task.objects.filter(usermail=c)
    username = registration.objects.filter(email= c)
    return render(request , 'project.html',{'username':username,'data':data}) 
def notifications(request):
    c=request.session['email']
    username= registration.objects.filter(email=c)
    data = task.objects.filter(usermail=c)
    return render(request,'notifications.html',{'username':username,'data':data}) 

# ------------------------------------Admin pannel----------------------------------- 

def adminhome(request):
    return render(request, 'admin.html') 

def adminlogin(request):
    if request.method =="POST":
        username = request.POST.get('usname')
        password = request.POST.get('password')
        authdata = User.objects.filter(username = username)
        if authdata:
            request.session['uname'] = username
            return redirect('adminprofile')
    return render(request,'admin.html')
def admindashboard(request):
    data = registration.objects.all()
    return render(request,'admindashboard.html',{'data':data})
def adminlogout(request):
    request.session.clear()
    return redirect('admin')
def adminproject(request):
    if request.method == "POST":
        taskname = request.POST.get('taskname')
        username = request.POST.get('user')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        taskdata = task(taskname=taskname,usermail=username,starttime=start_date,endtime=end_date)
        taskdata.save()
    data = registration.objects.all()
    return render(request,'adminproject.html',{'data':data})

def adminprofile(request):
    a = request.session['uname']
    data =  User.objects.filter(username = a)
    return render(request,'adminprofile.html',{'data':data})
def projectdetail(request):
    data = task.objects.all()
    return render(request,'projectdetail.html',{'data':data})
# def deletetask(request):

def delete(request,id):
    data = task.objects.get(id=id)
    data.delete()
    return redirect('projectdetail')
def adminfeedback(request):
    data = feedback.objects.all()
    return render(request, 'adminfeedback.html',{'data':data})
def deletefeed(request,id):
    data = feedback.objects.get(id=id)
    data.delete()
    return redirect('adminfeedback')
def deleteemp(request,id):
    data = registration.objects.get(id=id)
    data.delete()
    return redirect('admindash')


