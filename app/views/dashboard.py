from django.shortcuts import render
from django.views import View


from apps.connections.utils import check_status, get_qr_code
from apps.notifications.models import Notifications
from core.views import LoginRequiredMixinView


class DashboardView(LoginRequiredMixinView, View):
    def get(self, request):
        status = check_status() 
        notifications = Notifications.objects.all()
        qr = get_qr_code()
        context  = {
                "status": status,
                "notifications": notifications,
                "qr": qr,
        }
        return render(request, "dashboard/index.html",context)
