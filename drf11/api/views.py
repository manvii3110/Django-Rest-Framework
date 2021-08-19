from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


class StudentAPI(APIView):
   def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
         stu = Student.objects.get(pk=id)
         serializer = StudentSerializer(stu)
         return Response(serializer.data, status = status.HTTP_201_CREATED)
      stu = Student.objects.all()
      serializer = StudentSerializer(stu, m0any=True)
      return Response(serializer.data, status = status.HTTP_201_CREATED)

   def post(self, request, format=None):
      serializer = StudentSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Data posted'}, status = status.HTTP_201_CREATED) 
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

   def put(self, request, pk, format=None):  
      id = pk
      stu = Student.objects.get(pk=id)     
      serializer = StudentSerializer(stu, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Completed Data Updated'}, status = status.HTTP_201_CREATED) 
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

   def patch(self, request, pk, format=None):
      id = pk
      stu = Student.objects.get(pk=id)  
      serializer = StudentSerializer(stu, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Partially Data Updated'}, status = status.HTTP_201_CREATED) 
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

   def delete(self, request, pk, format=None):
      id = pk
      stu = Student.objects.get(pk=id) 
      stu.delete()
      return Response({'msg': 'Data Deleted'}, status = status.HTTP_201_CREATED)    

              
