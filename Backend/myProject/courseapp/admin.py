from django.contrib import admin
from .models import Department,Assignment,Submission,Course,Enrollment,Announcement

# Register your models here.
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Announcement)

