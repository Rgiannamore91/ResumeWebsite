# Generated by Django 5.0.6 on 2024-06-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['from_date'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['from_date'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('org', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
