# Generated by Django 5.1.2 on 2024-10-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('patient_id', models.CharField(max_length=50)),
                ('pathology_report', models.TextField()),
                ('radiology_image', models.ImageField(upload_to='radiology_images/')),
                ('cancer_stage', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('pathology_report', models.TextField()),
                ('radiology_image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
