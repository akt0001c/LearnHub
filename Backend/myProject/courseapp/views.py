from django.shortcuts import render
from rest_framework import viewsets,status
from courseapp import models
from courseapp import serializers
from rest_framework.response import Response



import requests

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
        ai_response_data= ai_response.get('choices', [{}])[0].get('text', '')
        ob= {
            'title': title,
            'description': description,
            'due_date': due_date,
            'course': course,
            'generated_details': ai_response_data
        }

        serializer= self.get_serializer(data=ob)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status= status.HTTP_201_CREATED)

        
    
    def generate_assignment(title,description,due_date,course):
        ai_url= 'https://api.openai.com/v1/chat/completions'
        ob={}
        prompt=""

        try:
            course_details= course.objects.get(course_code= course)
            course_name= course_details.course_name

            prompt = f"Generate an assignment with the following details:\nTitle: {title}\nCourse name: {course_name}\nDescription: {description}\nDue Date: {due_date}"

            ob={
              'prompt': prompt,
            }
        except course.DoesNotExist:
             raise ValueError(f"Course with ID {course} not found")
         

        headers = {
        'Authorization': 'Bearer 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',
        'Content-Type': 'application/json',
        }

        response= requests.post(ai_url,json=ob,headers=headers)


        if response.status_code== 200:
            return response.json()
        else:
            return {'assignment_content': 'AI model error: Unable to generate details'}
        
        




class SubmissionViewSets(viewsets.ModelViewSet):
    queryset=models.Submission.objects.all()
    serializer_class=serializers.SubmissionSerializer


class AnnouncementViewSets(viewsets.ModelViewSet):
    queryset= models.Announcement.objects.all()
    serializer_class=serializers.AnnouncementSerializer