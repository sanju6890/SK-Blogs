# Generated by Django 3.2.7 on 2021-09-21 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_remove_profile_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.post'),
        ),
    ]
