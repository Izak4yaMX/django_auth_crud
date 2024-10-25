from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "desc", "important"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write a title'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'})
                                            
        }
