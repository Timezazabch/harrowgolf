from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    tel = models.CharField(max_length=100)
    remark = models.CharField(max_length=255, blank=True)
    school_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()