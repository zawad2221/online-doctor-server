# Generated by Django 3.1.6 on 2021-05-08 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0002_auto_20210508_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='prescriptionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescribed_medicine', to='prescription.prescription'),
        ),
    ]