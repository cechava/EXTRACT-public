from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView

from .models import TravelAgentProfile


class ProfileListView(ListView):
    model = TravelAgentProfile
    template_name = 'profile_list.html'


class ProfileDetailView(DetailView):
    model = TravelAgentProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = TravelAgentProfile
    fields = ['keywords', 'profile', 'calendly_link']
    template_name = 'profile_update.html'
    success_url = reverse_lazy('agents:profile_detail')

    def get_object(self, queryset=None):
        return self.request.user.travelagentprofile