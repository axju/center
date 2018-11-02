from django import forms

from core.models import Project, ProjectReview

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'goal', 'percent', 'priority']
        widgets = {
            'percent': forms.NumberInput(attrs={'type':'range', 'step': '1'}),
        }

class ProjectReviewForm(forms.ModelForm):
    class Meta:
        model = ProjectReview
        fields = ['percent', 'priority', 'description']
        widgets = {
            'percent': forms.NumberInput(attrs={'type':'range', 'step': '1'}),
        }
