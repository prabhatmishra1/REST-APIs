from django.shortcuts import render
from rest_framework import viewsets
from . models import  Task
from . serailizers import TaskSerializer
# Create your views here.

# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
