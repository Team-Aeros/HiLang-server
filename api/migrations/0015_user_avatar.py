# Generated by Django 2.0.5 on 2018-06-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_course_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
