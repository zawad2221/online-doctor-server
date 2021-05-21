# Generated by Django 3.1.6 on 2021-05-21 22:19

from django.db import migrations, models
import django.db.models.deletion
import patient_report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pathology', '0001_initial'),
        ('prescription', '0007_auto_20210521_1651'),
        ('patient_report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('testId', models.AutoField(primary_key=True, serialize=False)),
                ('testRate', models.IntegerField()),
                ('pathologyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathology.pathology')),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('typeId', models.AutoField(primary_key=True, serialize=False)),
                ('typeName', models.CharField(max_length=111)),
            ],
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('testReportId', models.AutoField(primary_key=True, serialize=False)),
                ('testReportDetails', models.TextField()),
                ('issueDate', models.DateTimeField(blank=True, null=True)),
                ('isDone', models.BooleanField(default=False)),
                ('filePath', models.FileField(blank=True, null=True, upload_to=patient_report.models.TestReport.user_directory_path)),
                ('prescriptionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.prescription')),
                ('testId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_report.test')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='typeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_report.testtype'),
        ),
    ]