from django.contrib import admin
from django.urls import path
from oncology_ai.views import analyze_patient  # Adjust the import according to your app structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oncology_ai/analyze/', analyze_patient, name='analyze_patient'),
]
