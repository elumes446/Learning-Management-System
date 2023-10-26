# Generated by Django 4.2.2 on 2023-06-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0004_exam_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student'), ('admin', 'Admin')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]