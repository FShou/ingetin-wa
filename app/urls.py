from django.urls import path

from .views.notification import CreateNotificationView, EditNotificationView, delete_notification_view
from .views.auth import LoginView
from .views.dashboard import DashboardView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/notification/create", CreateNotificationView.as_view(), name="create-notification"),
    path("dashboard/notification/<str:id>/edit", EditNotificationView.as_view(), name="edit-notification"),
    path("dashboard/notification/<str:id>/delete", delete_notification_view, name="delete-notification"),
]
