from django.urls import path
from .views import survey_detail

urlpatterns = [
    path("assignment/<int:assignment_id>", survey_detail, name="survey_detail"),
]