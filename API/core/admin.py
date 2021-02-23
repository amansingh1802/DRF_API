from django.contrib import admin
from .models import Manager, Plan, SuscribedPlan

admin.site.register(Manager)
admin.site.register(Plan)
admin.site.register(SuscribedPlan)
