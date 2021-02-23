from django.db import models
from django.db.models import fields
from .models import Manager, Plan, SuscribedPlan
from rest_framework import serializers


class UserSerilizer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     try:
    #         print(' i am here called')
    #         user = Manager.objects.create_user(**validated_data)
    #     except TypeError:
    #         raise TypeError("kuch to hua he ")
    #     return user

    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'email',
                  'password', 'company', 'DOB', 'address']


class PlanSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SubscribedPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuscribedPlan
        fields = "__all__"
