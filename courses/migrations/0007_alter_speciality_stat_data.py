# Generated by Django 4.0.1 on 2022-02-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_speciality_stat_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='stat_data',
            field=models.DateField(),
        ),
    ]
