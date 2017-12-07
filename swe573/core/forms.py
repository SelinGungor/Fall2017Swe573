from django import forms
from core.models import Post
from django.forms import extras
from django.contrib.admin.widgets import AdminDateWidget


class HomeForm(forms.ModelForm):#with using ModelForm is connected to model
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = [
            'start_date',
            'end_date',
        ]