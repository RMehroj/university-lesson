from django import forms
from .models import Subject
from .models import Teacher
from django.forms import ModelForm
from django.views.generic.edit import FormView


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=256)
    code = forms.CharField(max_length=2048)
    stat_data = forms.DateTimeField()
    is_active = forms.BooleanField(required=True)


class TeacherCreateForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'degree', ]


class SubjectCreateForm(FormView):
    class Meta:
        model = Subject
        fields = ['name', 'specialities', 'teachers', ]
