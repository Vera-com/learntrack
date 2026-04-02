from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


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
            messages.success(request, "Study session added successfully!")
            return redirect('study_list')
    else:
        form = StudySessionForm()
    return render(request, 'tracker/add_session.html', {'form': form})


def edit_session(request, session_id):
    session = get_object_or_404(StudySession, id=session_id)

    if request.method == 'POST':
        form = StudySessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, "Study session updated successfully!")
            return redirect('study_list')
    else:
        form = StudySessionForm(instance=session)
    return render(request, 'tracker/edit_session.html', {'form': form})


def delete_session(request, session_id):
    session = get_object_or_404(StudySession, id=session_id)

    if request.method == 'POST':
        session.delete()
        messages.success(request, "Study session deleted successfully.")
        return redirect('study_list')

    return render(request, 'tracker/delete_session.html', {'session': session})
