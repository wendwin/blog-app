# Generated by Django 5.1.5 on 2025-01-23 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update',
            new_name='updated',
        ),
    ]
