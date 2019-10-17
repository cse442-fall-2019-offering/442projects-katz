from django.contrib import admin

# Register your models here.
from teamapp.models import School, EmailURL, Class, Team, Student, EnrolledIn, Teams

admin.site.register(School)
admin.site.register(EmailURL)
admin.site.register(Class)
admin.site.register(Team)
admin.site.register(Student)
admin.site.register(EnrolledIn)
admin.site.register(Teams)
