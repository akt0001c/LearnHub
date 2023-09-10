from django.urls import path,include
from rest_framework.routers import DefaultRouter
from courseapp import views

router= DefaultRouter()
router.register(r'department',views.DepartmentViewSets, basename='department')
router.register(r'courses',views.CourseViewSets,basename='courses')
router.register(r'enrollments',views.EnrollmentViewSets,basename='enrollment')
router.register(r'assignments',views.AssignmentViewSets,basename='assignments')
router.register(r'submissions',views.SubmissionViewSets,basename='submissions')
router.register(r'announcements',views.AnnouncementViewSets,basename='announcements')


urlpatterns=[
    path('',include(router.urls)),
]