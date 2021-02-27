from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)
    teacher = models.CharField(max_length=15, blank=False, null=False)
    loc = models.CharField(max_length=15, blank=False, null=False)
    content = models.CharField(max_length=100, blank=False, null=False)
    date = models.CharField(max_length=20, blank=False, null=False)
    img = models.ImageField(upload_to='images/%Y%m', blank=False, null=False)
    online = models.BooleanField(blank=False, default=False)
    sys = models.IntegerField(blank=False, null=False, default=0)  # soft delete

    class Meta:
        db_table = "course"

# class Student(models.Model):
#     name = models.CharField(max_length=10,blank=False,null=False)
#
#     desc = models.CharField(max_length=400,blank=False,null=False)
#     courseId = models.IntegerField(blank=False,null=False)

