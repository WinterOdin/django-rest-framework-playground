from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import task
# Create your views here.


@api_view(['get'])
def home(request):

    urls    =   {
        'list'  :'/jobs-list/',
        'detail':'/detail/<str:pk>/',
        'create':'/create/',
        'update':'/update/<str:pk>/',
        'delete':'/delete/<str:pk>/'
    }
    return Response(urls)

@api_view(['get'])
def taskList(request):
    
    taskData    =   task.objects.all().order_by('-id')
    serializer  =   taskSerializer(taskData,many=True)

    return Response(serializer.data)


@api_view(['get'])
def detailView(request,pk):
    
    taskData    =   task.objects.get(id=pk)
    serializer  =   taskSerializer(taskData,many=False)

    return Response(serializer.data)

@api_view(['post'])
def createView(request):
    
    serializer  =   taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('task')

    return Response(serializer.data)

@api_view(['POST'])
def updateView(request,pk):
    
    taskData    =   task.objects.get(id=pk)
    serializer  =   taskSerializer(instance=taskData,data=request.data)

    if serializer.is_valid():
        serializer.save()
        

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteView(request,pk):
    
    taskData    =   task.objects.get(id=pk)
    taskData.delete()
        
    return redirect('task')