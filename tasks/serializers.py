import datetime

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150, required=False)
    description = serializers.CharField(required=False)
    orderer_id = serializers.IntegerField(required=False)
    # orderer = serializers.CharField(source="orderer.user.username", max_length=150)
    executor_id = serializers.IntegerField(read_only=True, allow_null=True)
    # executor = serializers.CharField(source="executor.user.username", max_length=150)
    created_date =serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)
    closed_date = serializers.DateTimeField(read_only=True, allow_null=True)
    status = serializers.CharField(required=False, max_length=10)
    report = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.executor_id = validated_data.get("executor_id")
        instance.last_modified = validated_data.get("last_modified")
        instance.status = validated_data.get("status", instance.status)
        if instance.status == "finished":
            instance.closed_date = datetime.datetime.now()
            instance.report = validated_data.get("report", instance.report)
        instance.save()
        return instance


"""class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
"""