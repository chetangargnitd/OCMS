from django.contrib import admin

# Register your models here.
from .models import Complaint,Department, Complaint_Type, Property_Desc,Property
admin.site.register(Complaint)
admin.site.register(Department)
admin.site.register(Complaint_Type)
admin.site.register(Property)
admin.site.register(Property_Desc)
