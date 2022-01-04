from django.shortcuts import render
from ReserveApp.forms import Reserves

# Create your views here.


def reserve(request):

    form = Reserves()

    context = {'form': form}
    return render(request, 'ReserveApp/reserve.html', context)
