from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students", views.students, name="Student"),
    path("add_stud", views.student_add, name="AddStudent"),
    path("tests", views.tests, name='Test'),
    path("add_test", views.add_test, name="AddTest"),
    path("add_metatest", views.add_metatest, name="AddMetaTest"),
    path("update_student/<sID>", views.update_student, name="UpdateStudent"),
    path("update_test/<tID>", views.update_test, name="UpdateTest"),
    path("delete_student/<sID>", views.delete_student, name="DeleteStudent"),
    path("delete_test/<tID>", views.delete_test, name="DeleteTest"),
    path("stud_data", views.data_by_student, name="TestData"),
    path("subj_data", views.data_by_subject, name="SubjectDisp"),
]
