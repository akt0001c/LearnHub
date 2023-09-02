from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet
from django.urls import path,include

router = DefaultRouter()
router.register(r'instructors', InstructorViewSet)

urlpatterns=[
    path('',include(router.urls)),
    
]
