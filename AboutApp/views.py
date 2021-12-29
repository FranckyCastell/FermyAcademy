from django.shortcuts import render
from AboutApp.models import Users

# Create your views here.


def about(request):

    users = Users.objects.all()

    context = {'users': users}
    return render(request, 'AboutApp/about.html', context)
