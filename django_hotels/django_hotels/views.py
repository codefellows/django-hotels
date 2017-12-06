from django.shortcuts import render
from hotels.models import Hotel
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


@login_required(login_url=reverse_lazy('auth_login'))
@permission_required('hotels.view_hotel', login_url='/employees/login/')
def home_view(request):
    """The home page."""
    hotels = Hotel.objects.all()
    return render(request, 'django_hotels/home.html', {'hotels': hotels})


# @login_required(login_url=reverse_lazy('auth_login'))
# def cody_view(request):
#     hotels = Hotel.objects.all()
#     return render(request, 'django_hotels/home.html', {'hotels': hotels})

class CodyView(LoginRequiredMixin, ListView):
    model = Hotel
    context_object_name = 'hotels'
    template_name = 'django_hotels/home.html'
    login_url = '/employees/login/'
    # permission_required = 'hotels.view_hotel'

    def get_context_data(self, **kwargs):
        context = super(CodyView, self).get_context_data(**kwargs)
        context['malicious'] = """<script>
    function killAllHumans(){
        window.location = 'http://google.com'
    }
    killAllHumans()
</script>"""
        return context