# Generated by Django 3.2.7 on 2021-09-19 16:49

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=blog.models.Category),
        ),
    ]
