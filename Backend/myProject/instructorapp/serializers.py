from  rest_framework import serializers
from .models import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields=['name','gender','department','email','contact_no']