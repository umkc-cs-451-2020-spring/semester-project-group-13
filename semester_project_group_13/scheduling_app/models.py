import uuid
from django.db import models
from django_enumfield import enum
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy
from django.urls import reverse

class ProfessorType(enum.Enum):
    NON_TENURED = 1
    TENURED = 2
    PART_TIME_ADJUNCT = 3
    FULL_TIME_ADJUNCT = 4
    GRAD_TEACHING_ASST = 5
    
    __labels__ = {
        NON_TENURED: ugettext_lazy("Non-tenured Track"),
        TENURED: ugettext_lazy("Tenure-Track/Tenure"),
        PART_TIME_ADJUNCT: ugettext_lazy("Part-time Adjunct"),
        FULL_TIME_ADJUNCT: ugettext_lazy("Full-time Adjunct"),
        GRAD_TEACHING_ASST: ugettext_lazy("Graduate Teaching Assistant"),
    }

class School(enum.Enum):
    ARTS_AND_SCIENCES  = 1
    CONSERVATORY = 2
    HENRY_BLOCH_SCHOOL_OF_MANAGEMENT = 3
    SCHOOL_OF_BIOLOGICAL_AND_CHEMICAL_SCIENCES = 4
    SCHOOL_OF_COMPUTING_AND_ENGINEERING = 5
    SCHOOL_OF_EDUCATION = 6
    SCHOOL_OF_LAW = 7
    SCHOOL_OF_DENTISTRY = 8
    SCHOOL_OF_MEDICINE = 9
    SCHOOL_OF_NURSING_AND_HEALTH_STUDIES = 10
    SCHOOL_OF_PHARMACY = 11

    __labels__ = {
    ARTS_AND_SCIENCES: ugettext_lazy("College of Arts & Science"),
    CONSERVATORY: ugettext_lazy("Conservatory "),
    HENRY_BLOCH_SCHOOL_OF_MANAGEMENT: ugettext_lazy("Henry W. Bloch School of Management"),
    SCHOOL_OF_BIOLOGICAL_AND_CHEMICAL_SCIENCES: ugettext_lazy("School of Biological and Chemical Sciences"),
    SCHOOL_OF_COMPUTING_AND_ENGINEERING: ugettext_lazy("School of Computing & Engineering"),
    SCHOOL_OF_EDUCATION: ugettext_lazy("School of Education"),
    SCHOOL_OF_LAW: ugettext_lazy("School of Law"),
    SCHOOL_OF_DENTISTRY: ugettext_lazy("School of Dentistry"),
    SCHOOL_OF_MEDICINE: ugettext_lazy("School of Medicine"),
    SCHOOL_OF_NURSING_AND_HEALTH_STUDIES: ugettext_lazy("School of Nursing & Health Studies"),
    SCHOOL_OF_PHARMACY: ugettext_lazy("School of Pharmacy"),
    }


# Create your models here.
class Professor(models.Model):
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    professor_type = enum.EnumField(ProfessorType)
    school = enum.EnumField(School)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Constraint(models.Model):
    id = models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    # for the time unavailable field below, we need to figure out which times classes are available (such as 9 AM, 10 AM, etc) 
    # so that we can build out an enum like the school enum above. It will allow them to select a time (from a drop down menu) 
    # when they are unavailable which would make it much easier to represent time ranges of unavailability. Below is temporary 
    time_unavailable = models.TimeField()
    can_be_broken = models.BooleanField(default=True)

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.IntegerField()
    building = models.CharField(max_length=255)

    def __str__(self):
        return self.building + " " + str(self.room_number)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    section = models.IntegerField()
    school = enum.EnumField(School)

    def __str__(self):
        return self.course_name + " - " + '{:04}'.format(self.section)

    def __repr__(self):
        return self.course_name + " " + '{:04}'.format(self.section)

class Schedule(models.Model):  
    id = models.AutoField(primary_key=True) 
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # the same time field enum can be used here 
    time = models.TimeField()

    def __str__(self):
        return str(self.course) + " - " + str(self.professor) + " - " + str(self.time)