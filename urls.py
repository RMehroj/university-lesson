from django.urls import path
from .views import subjectcreate_view
from .views import speciality_create
from .views import speciality_view
from .views import subject_view
from .views import teacher_view
from .views import teachercreate_view

urlpatterns = [
        path("courses/subject/", subject_view, name='subjects'),
        path("courses/teacher/", teacher_view, name='teacher'),
        path("courses/speciality/", speciality_view, name='speciality'),
        path("courses/speciality/create/", speciality_create, name='speciality-view'),
        path("courses/teacher/create/", teachercreate_view, name='teachercreate-view'),
        path("courses/subject/create/", subjectcreate_view, name='subjectcreate-view'),
]
