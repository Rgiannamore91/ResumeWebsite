from django.shortcuts import render
firstName = "Ryan"
lastName = "Giannamore"

jobs = []
education_list = []
skills = []
projects = []
certificates = []

def base(request):
    return render(request, 'build/base.html')

def index(request):

    context = {
        "first": firstName,
        "last": lastName,
        "jobs": jobs,
        "education_list": education_list,
        "skills": skills,
        "projects": projects,
        "certificates": certificates,
    }
    return render(request, 'build/index.html', context)

