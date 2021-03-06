from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from alpha.views import IndexView, SignupView, ActivateView, PageView

from alpha.views import set_language

app_name = 'alpha'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('activate/<str:uidb64>/<str:token>/', ActivateView.as_view(), name='activate'),
    path('login/', LoginView.as_view(template_name='alpha/login.html', success_url='/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('page/<str:page>/', PageView.as_view(), name='page'),
    path('language/<str:language>', set_language, name='language-set'),
]
