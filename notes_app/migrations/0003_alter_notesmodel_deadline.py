# Generated by Django 3.2.4 on 2021-10-06 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_alter_notesmodel_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmodel',
            name='deadline',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
