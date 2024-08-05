from django.db import models



# Create your models here.
from profiles.models import Profile


class Task(models.Model):
    STATUS_CHOICES = (
        ("wait", "Waiting for executor"),
        ("in_process", "In process"),
        ("finished", "Finished"),
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    orderer = models.ForeignKey(Profile, related_name="created_tasks", null=True,  on_delete=models.CASCADE)
    executor = models.ForeignKey(Profile, related_name="taken_tasks", blank=True, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="wait")
    report = models.TextField(blank=True)
