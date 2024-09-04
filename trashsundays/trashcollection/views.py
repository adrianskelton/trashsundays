from django.db.models import Sum
from django.shortcuts import render, redirect  # Ensure these are imported
from .models import TrashCollection
from .forms import TrashCollectionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View  # Import the View class

def profile(request):
    total_bags = TrashCollection.objects.filter(user=request.user).aggregate(Sum('bags_collected'))['bags_collected__sum'] or 0
    return render(request, 'profile.html', {'total_bags': total_bags})

# Option 1: Function-based view (Keep this if you prefer function-based views)
def add_trash_collection(request):
    if request.method == 'POST':
        form = TrashCollectionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('profile')  # Redirect to a valid view name
    else:
        form = TrashCollectionForm()  # Instantiate an empty form
    
    return render(request, 'add_trash_collection.html', {'form': form})

# Option 2: Class-based view (Use this if you prefer class-based views)
class AddTrashCollectionView(LoginRequiredMixin, View):
    def get(self, request):
        form = TrashCollectionForm()
        return render(request, 'add_trash_collection.html', {'form': form})

    def post(self, request):
        form = TrashCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a valid view name
        return render(request, 'add_trash_collection.html', {'form': form})
