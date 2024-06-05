from django.db import models
from datetime import timedelta, datetime

class Summary(models.Model):
    body = models.TextField()

class Job(models.Model):
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    duration = models.DurationField(editable=False, blank=True, null=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.to_date is None:
            self.duration = datetime.now() - self.from_date
        else:
            self.duration = self.to_date - self.from_date

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["from_date"]

    def __str__(self):
        return  f"Job Title: {self.job_title}, Company: {self.company}"  
    
    @property
    def is_ongoing(self):
        return self.to_date is None  

    @property
    def duration_calculated(self):
        if self.to_date:
            return self.to_date - self.from_date
        return datetime.now() - self.from_date       

class Education(models.Model):
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    duration = models.DurationField(editable=False, blank=True, null=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.to_date is None:
            self.duration = datetime.now() - self.from_date
        else:
            self.duration = self.to_date - self.from_date

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["from_date"]

    def __str__(self):
        return f"School: {self.school}, Major: {self.major}"
    
    @property
    def is_ongoing(self):
        return self.to_date is None  

    @property
    def duration_calculated(self):
        if self.to_date:
            return self.to_date - self.from_date
        return datetime.now() - self.from_date    
    
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    org = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Projec Name: {self.project_name}, For: {self.org}"

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Skill: {self.name}"

class Certificate(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    link = models.URLField(max_length=500)

    def __str__(self):
        return f"Certificate: {self.name}, School: {self.school}"
