# Generated by Django 4.1.5 on 2023-01-15 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('group',), 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]