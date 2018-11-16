from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse
from django.urls import reverse_lazy

from core.models import Project, ProjectReview
from core.forms import ProjectForm, ProjectReviewForm


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description', 'goal', 'percent', 'priority']
    success_url = reverse_lazy('core:project-list')

    def get_form_class(self):
        return ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectList(LoginRequiredMixin, ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class ProjectPermission(LoginRequiredMixin, PermissionRequiredMixin):
    def has_permission(self):
        self.object = self.get_object()
        return self.object.user == self.request.user


class ProjectUpdate(ProjectPermission, UpdateView):
    model = Project
    fields = ['name', 'description', 'goal']


class ProjectDetail(ProjectPermission, DetailView):
    model = Project


class ProjectDelete(ProjectPermission, DeleteView):
    model = Project
    success_url = reverse_lazy('core:project-list')


class ProjectReviewCreate(ProjectPermission, CreateView):
    model = ProjectReview
    fields = ['percent', 'priority', 'description']

    def has_permission(self):
        return self.project.user == self.request.user

    def get_form_class(self):
        return ProjectReviewForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super(ProjectReviewCreate, self).get_initial()
        initial.update({'percent': self.project.percent,
                        'priority': self.project.priority,
                        })
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)
