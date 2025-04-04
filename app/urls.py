from django.urls import path

from app.views.connection import disconnect_view
from app.views.landing import landingpage_view

from .views.notification import (
    CreateNotificationView,
    EditNotificationView,
    delete_notification_view,
)
from .views.auth import LoginView, logout_view
from .views.dashboard import DashboardView

urlpatterns = [
    path("", landingpage_view, name="landing"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path(
        "dashboard/notification/create",
        CreateNotificationView.as_view(),
        name="create-notification",
    ),
    path(
        "dashboard/notification/<str:id>/edit",
        EditNotificationView.as_view(),
        name="edit-notification",
    ),
    path(
        "dashboard/notification/<str:id>/delete",
        delete_notification_view,
        name="delete-notification",
    ),
    path("connection/disconnect",disconnect_view,name="disconnect")
]
