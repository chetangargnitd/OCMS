from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import arrow
class Department(models.Model):
    dept_name=models.CharField(max_length=128)
    def __str__(self):
        return self.dept_name

class Complaint_Type(models.Model):
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
    complaint_type=models.CharField(max_length=50)
    def __str__(self):
        return self.complaint_type

class Property(models.Model):
    property_name=models.CharField(max_length=128)
    def __str__(self):
        return self.property_name

class Property_Desc(models.Model):
    property_name=models.ForeignKey(Property,on_delete=models.CASCADE,blank=True, null=True)
    room_name=models.CharField(max_length=50)

    def __str__(self):
        return '{}-{}' .format(self.property_name,self.room_name)
