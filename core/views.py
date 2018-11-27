from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse
from django.urls import reverse_lazy

from core.models import Category, Project, ProjectReview
from core.forms import ProjectForm, ProjectReviewForm


class UserPermission(LoginRequiredMixin, PermissionRequiredMixin):

    def has_permission(self):
        self.object = self.get_object()
        return self.object.user == self.request.user


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('core:category-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryList(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDelete(UserPermission, DeleteView):
    model = Category
    success_url = reverse_lazy('core:project-list')


class ProjectCreate(LoginRequiredMixin, FormView):
    template_name = 'core/project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('core:project-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ProjectList(LoginRequiredMixin, ListView):
    model = Project

    def get_queryset(self):
        filter = self.kwargs.get('filter')
        q = self.kwargs.get('q')

        queryset = Project.objects.filter(user=self.request.user)

        if filter and q:
            if filter == 'category':
                return queryset.filter(categorys__name=str(q))
            if filter == 'priority':
                return queryset.filter(priority=int(q))

        return queryset





class ProjectUpdate(UserPermission, UpdateView):
    model = Project
    fields = ['name', 'description','categorys']


class ProjectDetail(UserPermission, DetailView):
    model = Project


class ProjectDelete(UserPermission, DeleteView):
    model = Project
    success_url = reverse_lazy('core:project-list')


class ProjectReviewCreate(UserPermission, FormView):
    template_name = 'core/projectreview_form.html'
    form_class = ProjectReviewForm
    success_url = reverse_lazy('core:project-list')

    def has_permission(self):
        return self.project.user == self.request.user

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
        form.save()
        return super().form_valid(form)
