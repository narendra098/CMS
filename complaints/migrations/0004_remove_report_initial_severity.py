# Generated by Django 4.0.1 on 2022-01-14 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_remove_report_sub_incident_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='initial_severity',
        ),
    ]
