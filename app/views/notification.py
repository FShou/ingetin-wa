from django.shortcuts import redirect, render
from django.views import View
from apps.notifications.forms import NotificationsForm
from core.views import LoginRequiredMixinView


class NotificationView(LoginRequiredMixinView,View):
    def get(self,request):
        form = NotificationsForm()
        return render(request,"notification/index.html", { "form": form})

    def post(self,request):
        form = NotificationsForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)  
            notification.actor = request.user  
            notification.save()  
            return redirect(to="dashboard")
