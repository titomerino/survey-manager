from django.urls import path
from .views import (
    StudentCreateView,
    StudentUpdateView,
    StudentListView,
    student_delete_view
)

urlpatterns = [
    path("list/", StudentListView.as_view(), name="student_list"),
    path("new/", StudentCreateView.as_view(), name="student_create"),
    path("edit/<int:pk>/", StudentUpdateView.as_view(), name="student_edit"),
    path("delete/<int:pk>/", student_delete_view, name="student_delete"),
]