from django import forms
from hello.models import LogMessage


class SeatNumberForm(forms.Form):
    seat_number = forms.IntegerField(label='Номер места в плацкартном вагоне')

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

