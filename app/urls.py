from django.urls import path
from .views.test_send import TestSend
from .views.auth import LoginView
from .views.dashboard import DashboardView

urlpatterns = [
    path("", TestSend.as_view(), name="test_send"),
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
