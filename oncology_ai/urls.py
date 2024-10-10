from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('analyze/', views.analyze_patient, name='analyze_patient'),
]
