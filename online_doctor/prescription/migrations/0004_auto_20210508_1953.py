# Generated by Django 3.1.6 on 2021-05-08 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_auto_20210323_2030'),
        ('prescription', '0003_auto_20210508_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='appointmentId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment'),
        ),
    ]
