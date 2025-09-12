from django.urls import path, include
from . import views  # import your views file

urlpatterns = [
    path('',views.first_program, name='first'),
    path('student_register/', views.stu_reg, name="student_register"),
    path('register_details/', views.view_details, name="student_registers_detail"),
    path("student/<int:pk>/edit/", views.edit_student, name="student_edit"),
    path("student/<int:pk>/delete/", views.delete_student, name="student_delete"),
]           