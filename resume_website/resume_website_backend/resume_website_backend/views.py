"""from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView
"""
from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import *
from . models import *
from rest_framework.response import Response


class DetailsList(APIView):
    def get(self, request):
        output = [
            {
                "first": output.first,
                "last": output.last,
                "phone": output.phone,
                "email": output.email,
                "city": output.city,
                "state": output.state,
                "social_link": output.social_link,
                "summary": output.summary,
            }
            for output in Details.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class JobList(APIView):
    def get(self, request):
        output = [
            {
                "job_title": output.job_title,
                "company": output.company,
                "from_date": output.from_date,
                "to_date": output.to_date,
                "duration": output.duration,
                "duration_str": output.duration_str,
                "description": output.description,
            }
            for output in Job.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
class EducationList(APIView):
    def get(self, request):
        output = [
            {
                "school": output.school,
                "major": output.major,
                "from_date": output.from_date,
                "to_date": output.to_date,
                "degree": output.degree,
                "course_structure": output.course_structure,
            }
            for output in Education.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = EducationSerializer(data=request.data)

     

class ProjectList(APIView):
    def get(self, request):
        output = [
            {
                "project_name": output.project_name,
                "org": output.org,
                "role": output.role,
                "description": output.description,
                "github": output.github,
            }
            for output in Project.objects.all()
        ]
        return Response(output)
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)   

class LanguageList(APIView):
    def get(self, request):
        output = [
            {"name": output.name}
            for output in Language.objects.all()
        ]
        return Response(output)
    def post(self, request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 

class FrameWorkList(APIView):
    def get(self, request):
        output = [
            {"name": output.name}
            for output in FrameWork.objects.all()
        ]

    def post(self, request):
        serializer = FrameWorkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  

class SkillList(APIView):
    def get(self, request):
        output = [
            {"name": output.name}
            for output in Skill.objects.all()
        ]
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  
        
class CertificateList(APIView):
    def get(self, request):
        output = [
            {
                "name": output.name,
                "school": output.school,
                "link": output.link,
                "date": output.date,
            }
        ] 

    def post(self, request):
        serializer = CertificateSerializer(data=request.data)     
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  
        

"""
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
"""