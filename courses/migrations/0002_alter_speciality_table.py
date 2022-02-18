from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='speciality',
            table='Speciality',
        ),
    ]
