# Generated by Django 5.0.6 on 2024-06-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='is_right',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
