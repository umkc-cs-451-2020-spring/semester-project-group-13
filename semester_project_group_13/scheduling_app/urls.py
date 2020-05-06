from django.urls import path
from . import views
from .views import *

urlpatterns = [
     path('', views.home, name='schedule-home'),
     path('database/', views.database, name="schedule-database"),
     path('professor/new/', ProfessorCreateView.as_view(), name="professor-create"),
     path('professor/<uuid:pk>/update/', ProfessorUpdateView.as_view(), name="professor-update"),
     path('professor/<uuid:pk>/delete/', ProfessorDeleteView.as_view(), name="professor-delete"),
     path('room/new/', RoomCreateView.as_view(), name="room-create"),
     path('room/<int:pk>/update/', RoomUpdateView.as_view(), name="room-update"),
     path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name="room-delete"),
     path('course/new/', CourseCreateView.as_view(), name="course-create"),
     path('course/<int:pk>/update/', CourseUpdateView.as_view(), name="course-update"),
     path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name="course-delete"),
     path('generate/', views.generate, name="schedule-generate"),
     path('generated_schedule/', views.database, name="generated_schedule")
]
