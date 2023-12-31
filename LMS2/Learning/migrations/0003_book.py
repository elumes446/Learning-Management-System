# Generated by Django 4.2.2 on 2023-06-10 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to='books/')),
            ],
        ),
    ]
