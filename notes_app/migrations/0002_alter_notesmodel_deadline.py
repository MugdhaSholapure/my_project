# Generated by Django 3.2.4 on 2021-10-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmodel',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
