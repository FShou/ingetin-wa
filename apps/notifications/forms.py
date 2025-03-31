from django import forms
from .models import Notifications  

class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = [ 'title', 'description',  'recepiant', 'message', 'schedule_type', 'time', 'day_of_week', 'day_of_month', 'exact_datetime']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input input-primary w-full'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-primary w-full', 'rows': 4}),
            'recepiant': forms.TextInput(attrs={'class': 'input input-primary w-full'}),
            'message': forms.Textarea(attrs={'class': 'textarea textarea-primary w-full', 'rows': 4}),
            'schedule_type': forms.Select(attrs={'class': 'select select-primary w-full'}),
            'time': forms.TimeInput(attrs={'class': 'input input-primary w-full', 'type': 'time'}),
            'day_of_week': forms.NumberInput(attrs={'class': 'input input-primary w-full', 'min': 0, 'max': 6}),
            'day_of_month': forms.NumberInput(attrs={'class': 'input input-primary w-full', 'min': 1, 'max': 31}),
            'exact_datetime': forms.DateTimeInput(attrs={'class': 'input input-primary w-full', 'type': 'datetime-local'}),
        }
