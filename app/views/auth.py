from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            print(request.user)
            return redirect("dashboard")
        return render(request,"auth/login.html")

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")

        messages.error(request, "Invalid Credential")
        return render(request, "auth/login.html")

def logout_view(request):
    logout(request)
    return redirect(to="dashboard")
