from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from instructorapp import views
urlpatterns=[
    path('instructors/',views.InstructorList.as_view()),
    path('instructors/<int:pk>',views.InstructorCrud.as_view()),
]

urlpatterns= format_suffix_patterns(urlpatterns)

