# Generated by Django 3.1.6 on 2021-05-23 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_report', '0003_auto_20210521_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='testreport',
            name='typeId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient_report.testtype'),
            preserve_default=False,
        ),
    ]
