from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


#@api_view(['GET'])
#def hello_world(request):
#    return Response({'msg':'Hello World'})

@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
           stu = Student.objects.get(id=id)
           serializer = StudentSerializer(stu)
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    if request.method == 'POST':
      serializer = StudentSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Data posted'}, status = status.HTTP_201_CREATED) 
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

    if request.method == 'PUT':
      id = pk
      stu = Student.objects.get(pk=id)     
      serializer = StudentSerializer(stu, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Completed Data Updated'}, status = status.HTTP_201_CREATED) 
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

    if request.method == 'PATCH':
      id = pk
      stu = Student.objects.get(pk=id)  
      serializer = StudentSerializer(stu, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Partially Data Updated'}, status = status.HTTP_201_CREATED) 
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

    if request.method == 'DELETE':
      id = pk
      stu = Student.objects.get(pk=id) 
      stu.delete()
      return Response({'msg': 'Data Deleted'}, status = status.HTTP_201_CREATED)