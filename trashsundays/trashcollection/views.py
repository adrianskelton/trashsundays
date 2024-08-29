from django.shortcuts import render, redirect
from .models import TrashCollection
from .forms import TrashCollectionForm

def log_trash(request):
    if request.method == 'POST':
        form = TrashCollectionForm(request.POST)
        if form.is_valid():
            trash = form.save(commit=False)
            trash.user = request.user
            trash.save()
            return redirect('profile_view')
    else:
        form = TrashCollectionForm()
    return render(request, 'trashcollection/log_trash.html', {'form': form})