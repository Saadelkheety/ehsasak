# Generated by Django 3.0.7 on 2020-06-26 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20200626_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='Specialization',
            new_name='specialization',
        ),
        migrations.RenameField(
            model_name='specialization',
            old_name='Specialization',
            new_name='specialization',
        ),
    ]
