from datetime import timedelta
from django.db.models import Q
import requests
from django.utils import timezone

from apps.notifications.models import Notifications, ScheduleType
from core.settings import WAHA_BASE_URL


def send_wa(notification):
    url = f"{WAHA_BASE_URL}/api/sendText"
    data = {
        "session": "default",
        "chatId": f"{notification.recepiant}@c.us",
        "text": notification.message,
    }
    response = requests.post(url, json=data)
    # response.raise_for_status()
    print(response)



def get_tomorrow_notifications():
    tomorrow = timezone.now() + timedelta(days=1)
    today_weekday = tomorrow.weekday()  
    tomorrow_day = tomorrow.day
    tomorrow_month = tomorrow.month

    notifications = Notifications.objects.filter(
        Q(schedule_type=ScheduleType.DAILY)
        | Q(schedule_type=ScheduleType.WEEKLY, day_of_week=today_weekday)
        | Q(schedule_type=ScheduleType.MONTHLY, day_of_month=tomorrow_day)
        | Q(
            schedule_type=ScheduleType.EXACT,
            exact_datetime__month=tomorrow_month,
            exact_datetime__day=tomorrow_day,
        )
    )

    return notifications
