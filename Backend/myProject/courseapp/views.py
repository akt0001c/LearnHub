from django.shortcuts import render
from rest_framework import viewsets
from courseapp import models
from courseapp import serializers

# Create your views here.
class DepartmentViewSets(viewsets.ModelViewSet):
    queryset= models.Department.objects.all()
    serializer_class= serializers.DepartmentSerializer


class CourseViewSets(viewsets.ModelViewSet):
    queryset=models.Course.objects.all()
    serializer_class=serializers.CourseSerializer


class EnrollmentViewSets(viewsets.ModelViewSet):
    queryset=models.Enrollment.objects.all()
    serializer_class=serializers.EnrollmentSerializer


class AssignmentViewSets(viewsets.ModelViewSet):
    queryset=models.Assignment.objects.all()
    serializer_class=serializers.AssignmentSerializer

    def create(self, request, *args, **kwargs):
        title= request.data.get('title')
        description= request.data.get('description')
        due_date= request.data.get('due_date')
        course= request.data.get('course')

        ai_response= self.generate_assignment(title,description,due_date,course)

        return super().create(request, *args, **kwargs)
    
    def generate_assignment(title,description,due_date,course):
        ai_url= 'https://api.openai.com/v1/chat/completions'

        ob={
            'title': title,
        'description': description,
        'due_date': due_date,
        'course':course
        }

        headers = {
        'Authorization': 'Bearer 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',
        'Content-Type': 'application/json',
    }
        
        




class SubmissionViewSets(viewsets.ModelViewSet):
    queryset=models.Submission.objects.all()
    serializer_class=serializers.SubmissionSerializer


class AnnouncementViewSets(viewsets.ModelViewSet):
    queryset= models.Announcement.objects.all()
    serializer_class=serializers.AnnouncementSerializer