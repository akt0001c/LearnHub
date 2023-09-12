from rest_framework import serializers
from courseapp import models

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Department
        fields=['id','parent_department']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Course
        fields=['id','course_code','course_name','department','credits','description','instructor']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Enrollment
        fields=['id','student','course']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Assignment
        fields=['id','title','description','due_date','course','assignment_content']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Submission
        fields=['id','submission_date','status','remarks','student','assignment']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Announcement
        fields=['id','title','description','department','course']