# Generated by Django 3.0.6 on 2020-06-02 01:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notifications_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='last_checked',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
