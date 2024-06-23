from rest_framework.serializers import ModelSerializer
from .models import *

class DetailsSerializer(ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'first', 
            'last', 
            'phone', 
            'email', 
            'city', 
            'state', 
            'social_link', 
            'summary',
        ]
    
class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'job_title',
            'company',
            'from_date',
            'to_date',
            'duration',
            'duration_str',
            'description',
        ]

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'school',
            'major',
            'from_date',
            'to_date',
            'degree',
            'course_structure',
        ]

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'project_name',
            'org',
            'role',
            'description',
            'github',
        ]

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']

class FrameWorkSerializer(ModelSerializer):
    class Meta:
        model = FrameWork
        fields = ['name']

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill 
        fields = ['name']

class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            'name',
            'school',
            'link',
            'date',
        ]