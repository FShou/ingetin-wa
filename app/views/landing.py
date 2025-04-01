from django.shortcuts import redirect, render

def landingpage_view(request):
    if request.user.is_authenticated:
        return redirect(to="dashboard")
    return render(request,"index.html")

