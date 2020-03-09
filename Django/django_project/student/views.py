from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,get_user_model
from .forms import StudentRegisterForm,StudentLoginForm

def register(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            rollno= form.cleaned_data.get('rollno')

            messages.success(request,f'Your Account has been Created for {rollno}!Login now!')
            return redirect('student-login')
    else:
        form = StudentRegisterForm()
    return render(request,'student/register.html',{'form':form})

def studentlogin(request):
    form = StudentLoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)

            return redirect("blog-home")
        else:
            print("Error")
    return render(request,"student/login.html",context)
