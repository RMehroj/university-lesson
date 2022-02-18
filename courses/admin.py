from django.contrib import admin

from .models import Speciality, Subject
from courses.models import Teacher

admin.site.register(Speciality)
admin.site.register(Teacher)
admin.site.register(Subject)

