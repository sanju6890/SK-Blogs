# Generated by Django 3.2.7 on 2021-09-21 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_profile_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='posts',
        ),
    ]
