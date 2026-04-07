from django import forms
from .models import StudySession


class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['course', 'title', 'description', 'duration', 'date']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter session title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe what you studied...',
                'rows': 4
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter duration in minutes'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
