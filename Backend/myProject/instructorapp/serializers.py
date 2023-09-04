from  rest_framework import serializers
from .models import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields=['id','instructorName','gender','date_of_birth','department','email','contact_no']