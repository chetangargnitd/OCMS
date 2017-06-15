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


class Complaint(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    dd_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
    complaint_type=ChainedForeignKey(Complaint_Type,
                            chained_field="dept_name",
                            chained_model_field="dept_name",
                            show_all=False,
                            auto_choose=False,
                            sort=True,)
    property_name=models.ForeignKey(Property,on_delete=models.CASCADE,blank=True, null=True)
    room_name=ChainedForeignKey(Property_Desc,null=True, blank=True,
                            chained_field="property_name",
                            chained_model_field="property_name",
                            show_all=False,
                            auto_choose=False,
                            sort=True,)
    complaint_desc=models.CharField(max_length=1500,blank=False,null=False,default='code')

    def __str__(self):
        return '{}/{}/{}' .format(self.dept_name,self.complaint_type,self.auto_increment_id)
