# Generated by Django 2.0.5 on 2018-06-19 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_wordlistquestion_sentencestructure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lessonType',
        ),
    ]