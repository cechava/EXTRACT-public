from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView


from .models import TravelAgentProfile


class ProfileListView(ListView):
    model = TravelAgentProfile
    template_name = 'profile_list.html'


class ProfileDetailView(DetailView):
    model = TravelAgentProfile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = TravelAgentProfile
    fields = ['name', 'keywords', 'profile', 'calendly_link', 'image']
    template_name = 'profile_update.html'

    def get_object(self, queryset=None):
        return self.request.user.travelagentprofile

    def get_success_url(self):
        return reverse('agents:profile_detail', args=(self.object.pk,))


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("agents:login")
    template_name = "signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class HomeView(TemplateView):
    template_name = "home.html"
