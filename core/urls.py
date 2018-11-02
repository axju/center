from django.urls import path

from core.views import ProjectList, ProjectCreate, ProjectUpdate, ProjectDetail, ProjectDelete, ProjectReviewCreate

app_name = 'core'

urlpatterns = [
    #path('', IndexView.as_view(), name='index'),
    path('project/', ProjectList.as_view(), name='project-list'),
    path('project/create/', ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/review/', ProjectReviewCreate.as_view(), name='project-review'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
]
