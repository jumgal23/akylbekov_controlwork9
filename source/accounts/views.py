from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User


class UserCreateView(CreateView):
    template_name = 'user_create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('webapp:announcement_list')


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('webapp:announcement_list')


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_phone'] = self.request.user.profile.phone
        context['user_announcements'] = self.request.user.announcement_set.exclude(status='Удалено')
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile


class UserDetailView(DetailView):
    model = User  # Assuming you want to display details for a User model
    template_name = 'user_detail.html'  # Replace with the actual template file name
    context_object_name = 'user'  # The variable name in the template
