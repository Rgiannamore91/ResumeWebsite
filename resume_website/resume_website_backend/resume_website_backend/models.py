from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator, RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

class DetailsModel(models.Model):
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(
                f"There can be only one {self.__class__.__name__}, delete current instance in order to create a new one."
                )
        return super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        

class Details(DetailsModel):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    phone = models.CharField(
        max_length=10, 
        validators=[
            MinLengthValidator(10), 
            RegexValidator(r'^\d+$', 'Only numbers allowed')
        ]
    )
    email = models.CharField(
        max_length=254, 
        validators=[EmailValidator(message='Enter a valid email address.')]
    )
    summary = models.TextField()

class Job(models.Model):
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    duration = models.DurationField(editable=False, blank=True, null=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.from_date:
            if self.to_date is None:
                duration_days = (datetime.now().date() - self.from_date).days
            else:
                duration_days = (self.to_date - self.from_date).days
            
            years = duration_days // 365
            months = (duration_days % 365) // 30

            if years > 0:
                self.duration_str = f'{years} years, {months} months' if months > 0 else f'{years} years'
            else:
                self.duration_str = f'{months} months'
            self.duration = datetime.now().date() - self.from_date 
        super(Job, self).save(*args, **kwargs)

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
            self.duration = datetime.now().date() - self.from_date
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
