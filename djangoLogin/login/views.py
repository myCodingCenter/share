from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def index(request):
    return render(request, "login/index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            messages.error(request,"Invalid Cedentials! Please try again with correct credentials")
            return render(request,'login/login.html')
    return render(request,'login/login.html')
def logout_view(request):
     logout(request)
     messages.success(request,"logout successfully")
     return redirect('login_view')