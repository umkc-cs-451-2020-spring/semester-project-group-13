from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request, "scheduling_app/home.html")

def database(request):
    context = {
        "professors" : Professor.objects.all().order_by("last_name"),
        "rooms" : Room.objects.all().order_by("building", "room_number"),
        "courses" : Course.objects.all().order_by("course_name", "section")
    }
    return render(request, "scheduling_app/database.html", context)

class ProfessorCreateView(CreateView):
    model = Professor
    fields = ['first_name', 'last_name', "email", "professor_type", "school", "created_by"]
    success_url = reverse_lazy('schedule-database')

class ProfessorUpdateView(UpdateView):
    model = Professor
    fields = ['first_name', 'last_name', "email", "professor_type", "school", "created_by"]
    success_url = reverse_lazy('schedule-database')

class ProfessorDeleteView(DeleteView):
    model = Professor
    success_url = reverse_lazy('schedule-database')

class RoomCreateView(CreateView):
    model = Room
    fields = ['building', 'room_number']
    success_url = reverse_lazy('schedule-database')

class RoomUpdateView(UpdateView):
    model = Room
    fields = ['building', 'room_number']
    success_url = reverse_lazy('schedule-database')

class RoomDeleteView(DeleteView):
    model = Room
    fields = ['building', 'room_number']
    success_url = reverse_lazy('schedule-database')


class CourseCreateView(CreateView):
    model = Course
    fields = ['course_name', 'section', 'school']
    success_url = reverse_lazy('schedule-database')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_name', 'section', 'school']
    success_url = reverse_lazy('schedule-database')

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('schedule-database')

def generate(request):  
    return render(request, "scheduling_app/generate.html")