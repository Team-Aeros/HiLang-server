# Generated by Django 2.0.5 on 2018-05-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_language_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='flag',
            field=models.CharField(max_length=50, null=True),
        ),
    ]