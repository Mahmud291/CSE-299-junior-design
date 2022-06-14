from django.forms import  fields
from course.models import Course
class Courseform(form.Modelform):
    classmethod:
    model=Course
    fields =" "