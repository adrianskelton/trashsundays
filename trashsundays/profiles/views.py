# profiles/views.py
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    # You can pass context data to the template if needed
    context = {
        'user': request.user,
    }
    return render(request, 'users/profile.html', context)


def profile_view(request):
    user = request.user
    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    context = {
        'user': user,
        'greeting': greeting,
    }

    return render(request, 'users/profile.html', context)
