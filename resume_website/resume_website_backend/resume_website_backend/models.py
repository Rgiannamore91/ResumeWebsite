from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    duration = models.DurationField(blank=True, null=True)
    description = models.TextField()

class Education(models.Model):
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    duration = models.DurationField(blank=True, null=True)
    description = models.TextField()

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    org = models.CharField(max_length=50)
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Certificate(models.Moedl):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    link = models.URLField(max_length=500)
