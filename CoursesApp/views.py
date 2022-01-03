from django.shortcuts import render
from CoursesApp.models import Courses

# Create your views here.


def courses(request):
    courses = Courses.objects.all()

    context = {'courses': courses}
    return render(request, 'CoursesApp/courses.html', context)
