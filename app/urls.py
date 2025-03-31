from django.urls import path

from .views.notification import NotificationView
from .views.test_send import TestSend
from .views.auth import LoginView
from .views.dashboard import DashboardView

urlpatterns = [
    path("", TestSend.as_view(), name="test_send"),
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/notification/create", NotificationView.as_view(), name="notification"),
]
