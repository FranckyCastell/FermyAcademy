from django.shortcuts import render
from ProfileApp.models import Profile

# Create your views here.


def profile(request):

    #user = request.user.id
    profile = Profile.objects.filter(name=request.user.id)  # USER NAME (MODEL) X CURRENT USER (ID=1)

    context = {'profile': profile}
    return render(request, 'ProfileApp/profile.html', context)
