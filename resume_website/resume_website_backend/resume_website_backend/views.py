from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView

def base(request):
    return render(request, 'build/base.html')

def index(request):
    detail_list = Details.objects.all()
    details = detail_list[0]
    jobs = Job.objects.all()
    education_list = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    context = {
        "details": details,
        "jobs": jobs,
        "education_list": education_list,
        "skills": skills,
        "projects": projects,
        "certificates": certificates,
    }
    return render(request, 'build/index.html', context)


