from django.contrib.auth import forms
from django.forms import widgets
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, Textarea
from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
        }

