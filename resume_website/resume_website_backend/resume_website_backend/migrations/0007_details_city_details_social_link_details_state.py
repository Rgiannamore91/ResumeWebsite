# Generated by Django 5.0.6 on 2024-06-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_website_backend', '0006_job_duration_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='city',
            field=models.CharField(default='New York', max_length=50),
        ),
        migrations.AddField(
            model_name='details',
            name='social_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='state',
            field=models.CharField(default='NY', max_length=2),
        ),
    ]