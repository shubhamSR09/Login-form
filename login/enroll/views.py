from django.shortcuts import render,HttpResponseRedirect
from .form import SingUp
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def sing_up(request):
    fm =''
    hn = ''
    if request.method == 'POST':
        fm=SingUp(request.POST)
        if fm.is_valid():
            fm.save()
            hn = "Account Created Successfully"
        else:
            fm=SingUp()
    return render(request, 'enroll/singup.html',{'form':fm ,'hn':hn})


#login Views
def UserLogin(request):
    fm = ''
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username =uname, password =upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:

        fm = AuthenticationForm()
    return render(request, 'enroll/login.html',{'form':fm})


#profile views

def UserProfile(request):
    if request.user.is_authenticated:

        return render(request, 'enroll/profile.html' ,{'name':request.user})
    else:
        return HttpResponseRedirect('/user_login/')
#user Logout
def user_logout(request):
    logout
    return render(request, 'enroll/singup.html')