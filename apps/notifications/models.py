from django.db import models
from core.models import BaseModel


class ScheduleType(models.TextChoices):
    DAILY = "DA", "Daily"
    WEEKLY = "WE", "Weekly"
    MONTHLY = "MO", "Monthly"
    EXACT = "EX", "Exact"


class Notifications(BaseModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    recepiant = models.CharField(max_length=13)
    message = models.TextField(blank=True)
    schedule_type = models.CharField(
        max_length=2,
        choices=ScheduleType.choices,
        default=ScheduleType.DAILY,
    )
    time = models.TimeField(null=True, blank=True)
    day_of_week = models.IntegerField(null=True, blank=True)
    day_of_month = models.IntegerField(null=True, blank=True)
    exact_datetime = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

