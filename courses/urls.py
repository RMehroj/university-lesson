
from django.urls import path
from .views import speciality_create
from .views import speciality_view
from .views import teacher_view
from .views import subject_view
from .views import teacher_create
from .views import subject_create


urlpatterns = [
    path("courses/subject/", subject_view, name='subjects'),
    path("courses/teacher/", teacher_view, name='teacher'),
    path("courses/speciality/", speciality_view, name='speciality'),
    path("courses/speciality/create/", speciality_create, name='speciality-view'),
    path("courses/teacher/create/", teacher_create, name='teacher-create'),
    path("courses/subject/create/",subject_create, name='subject-create'),
]
