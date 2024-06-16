from django.shortcuts import render, get_object_or_404
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
    context = {
        "details": details,
        "jobs": jobs,
        "education_list": education_list,
        "languages_str": languages_str,
        "frameworks_str": frameworks_str,
        "skills_str": skills_str,
        "projects": projects,
    }
    return render(request, 'build/index.html', context)

def work_experience(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {
        "job": job,
    }
    return render(request, 'build/work_experience.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        "project": project,
    }
    return render(request, 'build/project_detail.html', context)

def certificate_page(request):
    certificates = Certificate.objects.all()
    context = {
        "certificates": certificates,
    }
    return render(request, 'build/certificate_page.html', context)