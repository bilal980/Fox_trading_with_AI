from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def handlesignup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # gender=request.POST['gender']
        username=fname+lname

        if len(username) > 15 or len(username)< 4 :
            messages.error(request,"Name must be between 3 to 15 characters")
            return redirect('/signup')
        if not username.isalnum():
            messages.error(request,'User Name must  contain Number and Letters')
            return redirect('/signup')
        if pass1!=pass2:
            messages.error(request,'Password do not match')
            return redirect('/signup')
        

        myuser=User.objects.create(username=email,email=email,password=pass1,first_name=fname,last_name=lname)
        myuser.save()
        messages.success(request,"Congratulations Your acount has been succeessfully created!")
        return redirect('/')
    else:
        return HttpResponse("404 Not Found !")
    
    