from django import forms
from .models import Speciality
from .models import Teacher


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=256)
    code = forms.CharField(max_length=2048)
    stat_data = forms.DateTimeField()
    is_active = forms.BooleanField(required=True)


class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    degree = forms.CharField(max_length=256)


class SubjectForm(forms.Form):
    name = forms.CharField(max_length=256)
    Specialities = forms.ManyToManyField(Speciality)
    teachers = forms.ManyToManyField(Teacher)
