# Generated by Django 4.2.2 on 2023-06-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0008_remove_user_role_user_is_admin_user_is_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_customer',
            new_name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Is admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Is employee'),
        ),
    ]