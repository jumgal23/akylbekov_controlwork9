from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Announcement, Comment
from .forms import AnnouncementForm, CommentForm


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement_list.html'
    context_object_name = 'announcements'


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcement_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(announcement_com=self.object)
        return context


class AnnouncementUpdateView(LoginRequiredMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement_form.html'


class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'announcement_delete.html'
    success_url = reverse_lazy('webapp:announcement_list')



class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        # Assuming 'announcement_com' is the ForeignKey field in Comment model
        announcement_id = self.object.announcement_com_id
        return reverse_lazy('webapp:announcement_detail', kwargs={'pk': announcement_id})


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement_form.html'
    success_url = reverse_lazy('webapp:announcement_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.announcement_com_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:announcement_detail', kwargs={'pk': self.kwargs['pk']})
