from django import forms
from .models import StudySession


class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['course', 'title', 'description', 'duration', 'date']
