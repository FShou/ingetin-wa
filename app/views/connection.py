from django.shortcuts import redirect
from django.views import View
import requests
from core.settings import WAHA_BASE_URL
from core.views import LoginRequiredMixinView

def disconnect_view(request):
    requests.post(f"{WAHA_BASE_URL}/api/sessions/default/logout")
    return redirect(to="dashboard")
