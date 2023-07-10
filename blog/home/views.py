from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

#authentication system

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser = User.objects.create_user(username=username, password=password)
        myuser.first_name=name
        myuser.save()
        messages.success(
            request, f" User {name} has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            # Redirect to a success page
            messages.success(
                request, f"{user.first_name} has been successfully loggedIn")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404 - Not found")
def userlogout(request):
    logout(request)
    return redirect('home')
