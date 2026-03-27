from django.contrib import admin

from .models import StudySession, Course


admin.site.register(Course)
admin.site.register(StudySession)
