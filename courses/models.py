from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=2048)
    stat_data = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Speciality'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    degree = models.CharField(max_length=256)

    class Meta:
        db_table = 'Teacher'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Subject(models.Model):
    name = models.CharField(max_length=256)
    Specialities = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)

    class Meta:
        db_table = 'Subject'

    def __str__(self):
        return f'{self.name}'


