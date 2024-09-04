from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import UserRegisterForm, ProfileUpdateForm
from trashcollection.models import TrashCollection  # Import the TrashCollection model

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    # Calculate the total number of trash bags collected by the user
    total_bags = TrashCollection.objects.filter(user=request.user).aggregate(Sum('bags_collected'))['bags_collected__sum'] or 0

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'users/profile.html', {'form': form, 'total_bags': total_bags})

def home(request):
    # Aggregate the total amount of trash collected by all users
    total_trash_picked_up = TrashCollection.objects.aggregate(total=Sum('bags_collected'))['total'] or 0

    return render(request, 'home.html', {'total_trash_picked_up': total_trash_picked_up})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile_view(request):
    return render(request, 'users/profile.html')

