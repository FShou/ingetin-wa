from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views import View
from app.views import dashboard
from apps.notifications.forms import NotificationsForm
from apps.notifications.models import Notifications
from core.views import LoginRequiredMixinView


class CreateNotificationView(LoginRequiredMixinView, View):
    def get(self, request):
        form = NotificationsForm()
        return render(request, "notification/index.html", {"form": form})

    def post(self, request):
        form = NotificationsForm(request.POST)
        if not form.is_valid():
            return render(request, "notification/index.html", {"form": form})

        notification = form.save(commit=False)
        notification.actor = request.user
        notification.save()
        return redirect(to="dashboard")


class EditNotificationView(LoginRequiredMixinView, View):
    def get(self, request, id):
        notification = get_object_or_404(Notifications, id=id)
        if not request.user == notification.actor:
            return redirect(to="dashboard")
        form = NotificationsForm(instance=notification)
        return render(request, "notification/edit.html", {"form": form})

    def post(self, request, id):
        notification = get_object_or_404(Notifications, id=id)
        if not request.user == notification.actor:
            return redirect(to="dashboard")
        form = NotificationsForm(request.POST, instance=notification)
        if not form.is_valid():
            return render(request, "notification/edit.html", {"form": form})
        notification = form.save()
        return redirect(to="dashboard")


@login_required()
def delete_notification_view(request, id):
    notification = get_object_or_404(Notifications, id=id)
    if not request.user == notification.actor:
        return redirect(to="dashboard")
    notification.delete()
    return redirect(to="dashboard")
