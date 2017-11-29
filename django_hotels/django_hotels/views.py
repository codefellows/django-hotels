from django.shortcuts import render
from hotels.models import Hotel


def home_view(request):
    """The home page."""
    hotels = Hotel.objects.all()
    return render(request, 'django_hotels/home.html', {'hotels': hotels})
