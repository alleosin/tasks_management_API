import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Task
from .serializers import TaskSerializer

from itertools import chain

"""class TasksViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer"""


"""class TasksAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
"""

class TasksAPIView(APIView):
    def get(self, request):
        t = Task.objects.all()
        if request.user.groups.filter(name="Customer").exists():
            req_user_prof = request.user.profile
            t = Task.objects.filter(orderer=req_user_prof)
        elif request.user.groups.filter(name="Employee").exists():
            req_user_prof = request.user.profile
            taken_tasks = Task.objects.filter(executor=req_user_prof)
            untaken_tasks = Task.objects.filter(status="wait")
            t = list(chain(taken_tasks, untaken_tasks))
        return Response({"tasks": TaskSerializer(t, many=True).data})

    def post(self, request):
        if request.user.groups.filter(name="Customer").exists():
            serializer = TaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save(
                orderer_id=request.user.profile.id,
                executor_id=None,
                closed_date=None,
                status="wait",
                report=""
            )
        return Response({"task": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TaskSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            executor_id=request.user.profile.id
            )
        return Response({"post": serializer.data})
