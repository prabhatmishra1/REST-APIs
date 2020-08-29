from rest_framework import serializers
from . models import  Task

# Serializers define the API representation.
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed']
