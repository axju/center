from django.db import models
from django.conf import settings
from django.urls import reverse

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=256)
    description = models.TextField(default='')
    goal = models.TextField()

    priority = models.IntegerField(default=8, choices=[(i,str(i)) for i in range(11)])
    percent = models.IntegerField(default=5)

    class Meta:
        ordering = ['-priority', '-percent']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:project-detail', args=[str(self.id)])


class ProjectReview(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    create_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=8, choices=[(i,str(i)) for i in range(11)])
    percent = models.IntegerField(default=5)
    description = models.TextField(default='')

    class Meta:
        ordering = ['-create_at']

    def save(self, *args, **kwargs):
        super(ProjectReview, self).save(*args, **kwargs)

        if self.percent == 100:
            self.priority = 0
            super(ProjectReview, self).save(*args, **kwargs)

        self.project.priority = self.priority
        self.project.percent = self.percent
        self.project.save()

    def get_absolute_url(self):
        return reverse('core:project-detail', args=[str(self.project.id)])
