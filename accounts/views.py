from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("articles:home")
        else: 
            print("Invalid credentials")
        
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("articles:home")

def register_view(request):
    pass