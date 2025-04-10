from django.contrib import admin

from .models import User, Reporter, Article, Publication, Admin, Event, Student, Event_approver, Attendance

admin.site.register(User)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Admin)
admin.site.register(Event)
admin.site.register(Student)
admin.site.register(Event_approver)
admin.site.register(Attendance)
