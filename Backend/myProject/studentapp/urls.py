from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from studentapp import views

urlpatterns=[
    path('students/',views.StudentList.as_view()),
    path('students/<int:pk>',views.studentCrud.as_view())
]

urlpatterns= format_suffix_patterns(urlpatterns)