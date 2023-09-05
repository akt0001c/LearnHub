from  rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','studentId','studentName','gender','date_of_Birth','major','email','contact_number']