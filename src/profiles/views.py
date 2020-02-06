from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def user_profile_name(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
    else:
        profile = 'no profile'

    context = {
        'user': profile
    }

    return render(request, 'profiles/test.html', context)

def hello_world(request):
    hw = "Hello World"
    return HttpResponse(hw)