from django.urls import path

from core.views import CategoryList, CategoryCreate, CategoryDelete, ProjectList, ProjectCreate, ProjectUpdate, ProjectDetail, ProjectDelete, ProjectReviewCreate

app_name = 'core'

urlpatterns = [
    #path('', IndexView.as_view(), name='index'),
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/create/', CategoryCreate.as_view(), name='category-create'),
    path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='category-delete'),
    path('project/', ProjectList.as_view(), name='project-list'),
    path('project/filter/<str:filter>/<str:q>/', ProjectList.as_view(), name='project-list'),
    path('project/create/', ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/review/', ProjectReviewCreate.as_view(), name='project-review'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
]
