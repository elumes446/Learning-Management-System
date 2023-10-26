# Generated by Django 4.2.2 on 2023-06-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0007_remove_user_is_admin_remove_user_is_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Is admin'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='Is customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Is employee'),
        ),
    ]
