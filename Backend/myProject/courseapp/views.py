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


class SubmissionViewSets(viewsets.ModelViewSet):
    queryset=models.Submission.objects.all()
    serializer_class=serializers.SubmissionSerializer


class AnnouncementViewSets(viewsets.ModelViewSet):
    queryset= models.Announcement.objects.all()
    serializer_class=serializers.AnnouncementSerializer