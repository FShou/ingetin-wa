from django import forms
from .models import Notifications  

class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['recepiant', 'message', 'schedule_type', 'time', 'day_of_week', 'day_of_month', 'exact_datetime']
        widgets = {
            'recepiant': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'message': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full', 'rows': 4}),
            'schedule_type': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'time': forms.TimeInput(attrs={'class': 'input input-bordered w-full', 'type': 'time'}),
            'day_of_week': forms.NumberInput(attrs={'class': 'input input-bordered w-full', 'min': 0, 'max': 6}),
            'day_of_month': forms.NumberInput(attrs={'class': 'input input-bordered w-full', 'min': 1, 'max': 31}),
            'exact_datetime': forms.DateTimeInput(attrs={'class': 'input input-bordered w-full', 'type': 'datetime-local'}),
        }
