from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_request(request):
    if request.method == "POST":
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request,user)
            return redirect("register")
    form = NewUserForm()
    return render(request, "register.html", {"register_form": NewUserForm()})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password=password)
            if user is not None:
                login(request,user)
                return redirect("all_active_books")
            else:
                pass
        else:
            pass
    form = AuthenticationForm()
    return render(request,"login.html",{"login_form":AuthenticationForm()})   

def logout_request(request):
    logout(request)
    return redirect("login_user")             

	
		
    