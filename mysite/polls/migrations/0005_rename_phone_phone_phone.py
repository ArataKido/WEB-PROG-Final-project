# Generated by Django 4.0.2 on 2022-04-18 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_task_email_email_rename_task_message_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='Phone',
            new_name='phone',
        ),
    ]
