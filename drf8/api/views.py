from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

#@api_view(['GET'])
#def hello_world(request):
#    return Response({'msg':'Hello World'})

@api_view(['GET','POST', 'PUT', 'DELETE'])
def hello_world(request):
    if request.method == 'GET':
      return Response({'msg':'This is GET Request'})
    if request.method == 'POST':
      #print(request.data)
      return Response({'msg':'This is POST Request', 'data':request.data})
