# Generated by Django 3.2.7 on 2021-09-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210916_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]