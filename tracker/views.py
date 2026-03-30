from django.shortcuts import render

from .models import StudySession


def study_list(request):
    sessions = StudySession.objects.all()
    return render(request, 'tracker/study_list.html', {'sessions': sessions})
