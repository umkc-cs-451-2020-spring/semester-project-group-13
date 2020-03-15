from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='schedule-home'),
     path('database/', views.database, name="schedule-database"),
     path('generate/', views.generate, name="schedule-generate")
]
