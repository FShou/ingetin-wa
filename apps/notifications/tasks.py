from datetime import datetime, timedelta
from apps.notifications.methods import get_tomorrow_notifications, send_wa
from huey.contrib.djhuey import db_periodic_task, task
from huey import crontab


@task
def send_wa_task(notification):
    send_wa(notification)


@db_periodic_task(crontab(hour="1"))
def schedule_tomorrow_notifications_tasks():
    notifications = get_tomorrow_notifications()
    tomorrow = datetime.now() + timedelta(days=1)  # Get tomorrow's date
    for notif in notifications:
        time_str = notif.time if notif.time is not None else "00:00"

        hour, minute = map(int, time_str.split(":"))

        notif_datetime = tomorrow.replace(
            hour=hour, minute=minute, second=0, microsecond=0
        )

        send_wa_task(notif).schedule(eta=notif_datetime)
