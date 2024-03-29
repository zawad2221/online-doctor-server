# Generated by Django 3.1.6 on 2021-04-30 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientQuery',
            fields=[
                ('queryId', models.AutoField(primary_key=True, serialize=False)),
                ('queryDetails', models.TextField()),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
