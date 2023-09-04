from django.shortcuts import render

# Create your views here.


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Instructor
from .serializers import InstructorSerializer
class InstructorList(APIView):
#this class will have to methods 
#1. Get all the instructors
#2. Create a new Instructor

    def get(self,request,format=None):
        instructors= Instructor.objects.all()
        serializer= InstructorSerializer(instructors,many=True)
        return Response(serializer.data)
    
    def post(self,request,fromat=None):
        serializer= InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    

class InstructorCrud(APIView):
    #this class for retrive , update and delete the instructor using primary key
    def get_object(self,pk):
        try:
            return Instructor.objects.get(pk=pk);
        except Instructor.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        instructor= self.get_object(pk)
        serializer= InstructorSerializer(instructor)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        instructor= self.get_object(pk)
        serializer= InstructorSerializer(instructor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        instructor= self.get_object(pk)
        instructor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




