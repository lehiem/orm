
# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

from orm.faker import Faker

import random 

fake = Faker()

# student
for _ in range(50):
    student = Student(
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    position = fake.jobTitle(),
    graduation_year = fake.year(),
    student_email = fake.email(),
    )
    student.save()

# attendance
for _ in range(50):
    student_id = random.choice(Student.objects.all())
    attendance = Attendance(
        date = fake.date(),
        attendance_status = fake.boolean(),
        student_id = student_id,

    )

# event
for _ in range(50):
    event = Event(
    event_name = fake.bio(),
    event_start = fake.date(),
    event_end = fake.date(),
    event_coordinator = fake.last_name(),
    approval = fake.boolean(),

    )

#admin
for _ in range(50):
    admin = Admin(
    admin_email = fake.email(),
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    job_title = fake.jobTitle(),
    room_number = fake.int(400),
    
    )

# join table 
for _ in range(50):
    event_name = random.choice(Event.objects.all())
    admin_email = random.choice(Admin.objects.all())
    event_approver = Event_approver(
    event_name = event_name,
    admin_email = admin_email, 
    individual_approval_status = fake.boolean(),

    )