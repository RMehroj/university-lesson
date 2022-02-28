from django.contrib import admin
from .models import Speciality, Subject
from courses.models import Teacher


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code',)
    list_display = ('name', 'code', 'stat_data', 'is_active',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_filter = ("degree",)
    list_display = ('first_name', 'last_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('teachers', 'name',)
    # 4-savolda shuni ichida 'specialities' ishlamadi.
    autocomplete_fields = ('specialities', 'teachers',)
    # list_select_related = ("specialities", 'teachers',) bu ham ishlamadi.
