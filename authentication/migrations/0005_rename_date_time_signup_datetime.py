# Generated by Django 5.0.3 on 2024-04-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_signup_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='date_time',
            new_name='datetime',
        ),
    ]