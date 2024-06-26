# Generated by Django 5.0.6 on 2024-06-05 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_website_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='duration',
            field=models.DurationField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='duration',
            field=models.DurationField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
