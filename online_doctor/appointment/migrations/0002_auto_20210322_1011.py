# Generated by Django 3.1.6 on 2021-03-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointmentSerialNumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmentPatientSymptomNote',
            field=models.TextField(),
        ),
    ]
