# Generated by Django 4.2.7 on 2024-11-25 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Housework', '0010_housework_calendar_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housework',
            name='calendar_event',
        ),
    ]