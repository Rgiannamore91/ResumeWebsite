"""
URL configuration for resume_website_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import url
from . views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/', DetailsList.as_view(), name="details"),
    path('jobs/', JobList.as_view(), name="jobs"),
    path('educations/', EducationList.as_view(), name="educations/"),
    path('projects/', ProjectList.as_view(), name="projects"),
    path('languages/', LanguageList.as_view(), name="languages"),
    path('frameworks/', FrameWorkList.as_view(), name="frameworks"),
    path('skills/', SkillList.as_view(), name="skill"),
    path('certificates/', CertificateList.as_view(), name="certificate/"),
    # path('', views.index, name='index'),
    # path('base/', views.base, name='base'),
    # path('job/<int:job_id>', views.work_experience, name='work_experience'),
    # path('project/<int:project_id>', views.project_detail, name='project_detail'),
    # path('certificate_page/', views.certificate_page, name='certificate_page'),
    # path('api-auth/', include('rest_framework.urls'))
]
