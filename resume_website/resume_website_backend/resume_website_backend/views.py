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
    languages = Language.objects.all()
    languages_str = ""
    for language in languages:
        languages_str += f"{language.name}; "
    frameworks = FrameWork.objects.all()
    frameworks_str = ""
    for framework in frameworks:
        frameworks_str += f"{framework.name}; "
    skills = Skill.objects.all()
    skills_str = ""
    for skill in skills:
        skills_str += f"{skill.name}; "
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    context = {
        "details": details,
        "jobs": jobs,
        "education_list": education_list,
        "languages_str": languages_str,
        "frameworks_str": frameworks_str,
        "skills_str": skills_str,
        "projects": projects,
        "certificates": certificates,
    }
    return render(request, 'build/index.html', context)


