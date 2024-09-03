from django.db.models import Sum
from .models import TrashCollection

@login_required
def profile(request):
    total_bags = TrashCollection.objects.filter(user=request.user).aggregate(Sum('bags_collected'))['bags_collected__sum'] or 0
    return render(request, 'profile.html', {'total_bags': total_bags})