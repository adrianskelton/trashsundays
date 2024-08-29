# profiles/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    # You can pass context data to the template if needed
    context = {
        'user': request.user,
    }
    return render(request, 'users/profile.html', context)