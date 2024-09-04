from django.db.models import Sum
from .models import TrashCollection
from .forms import TrashCollectionForm
from django.views import View  # Import the View class

def profile(request):
    total_bags = TrashCollection.objects.filter(user=request.user).aggregate(Sum('bags_collected'))['bags_collected__sum'] or 0
    return render(request, 'profile.html', {'total_bags': total_bags})

def add_trash_collection(request):
    if request.method == 'POST':
        form = TrashCollectionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('some_view_name')  # Redirect to a success page or another view
    else:
        form = TrashCollectionForm()  # Instantiate an empty form
    
    return render(request, 'add_trash_collection.html', {'form': form})

class TrashCollection(View):
    def get(self, request):
        form = TrashCollectionForm()
        return render(request, 'add_trash_collection.html', {'form': form})

    def post(self, request):
        form = TrashCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')  # Redirect to a valid view name
        return render(request, 'add_trash_collection.html', {'form': form})