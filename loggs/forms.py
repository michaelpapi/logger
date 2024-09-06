from django import forms

from .models import Logg, Loggs

class LoggForm(forms.ModelForm):
    class Meta:
        model = Logg
        fields = ['text']
        labels = {'text': ''}


class LogsForm(forms.ModelForm):
    class Meta:
        model = Loggs
        fields = ['text']
        labels={'text':'Loggs:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
