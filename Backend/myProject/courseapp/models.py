from django.db import models
from instructorapp.models import Instructor
from studentapp.models import Student

# Create your models here.

class Department(models.Model):
    deptName= models.CharField(max_length=100)
    parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
         db_table="Department"


class Course(models.Model):
    course_code= models.CharField(max_length=20)
    course_name= models.CharField(max_length=300)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)
    credits= models.PositiveIntegerField()
    description=models.TextField()
    instructor= models.ForeignKey(Instructor,on_delete=models.CASCADE)
    class Meta:
         db_table="Course"


class Enrollment(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    class Meta:
         db_table="Enrollment"

    def __str__(self):
        return f"{self.student} : {self.course}"
    

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
         db_table="Assignment"


class Submission(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Late', 'Late'),
        ('Graded', 'Graded'),
    ]

    submission_date= models.DateField()
    status= models.CharField(max_length=20,choices=STATUS_CHOICES)
    remarks= models.TextField()
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    class Meta:
         db_table="Submission"


class Announcement(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        publish_date = models.DateField()
        department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
        course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
        class Meta:
         db_table="Announcement"