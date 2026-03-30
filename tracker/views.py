from django.shortcuts import render, redirect

from .models import StudySession
from .forms import StudySessionForm


def study_list(request):
    sessions = StudySession.objects.all()
    return render(request, 'tracker/study_list.html', {'sessions': sessions})


def add_session(request):
    if request.method == 'POST':
        form = StudySessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudySessionForm()
    return render(request, 'tracker/add_session.html', {'form': form})
