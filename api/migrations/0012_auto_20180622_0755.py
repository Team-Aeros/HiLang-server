# Generated by Django 2.0.5 on 2018-06-22 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20180619_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=1, max_digits=3)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lessoncompleted',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
