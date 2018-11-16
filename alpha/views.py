from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate

from alpha.tokens import account_activation_token

from django.utils import translation

from django.contrib.auth.forms import AuthenticationForm

from django.http import Http404
from django.utils.translation import ugettext_lazy as _

from django.core.mail import send_mail
from django.contrib import messages

from alpha.forms import SignupForm

from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.dispatch import receiver



@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'You have been logged out. Have a nice day.')

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'Hello {}, nice to see you :)'.format(request.user))

def set_language(request, language):
    next_url = request.GET.get('next', '/')
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect(next_url)

class IndexView(View):
    def get(self, request):
        signup_form = SignupForm()
        login_form = AuthenticationForm()
        return render(request, 'alpha/index.html', {'signup_form': signup_form, 'login_form': login_form})


class PageView(View):
    def get(self, request, *args, **kwargs):
        try:
            return render(request, 'alpha/pages/{}.html'.format(kwargs.get('page')))
        except:
            raise Http404(_('Page does not exist'))


class SignupView(FormView):
    template_name = 'alpha/signup.html'
    form_class = SignupForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        user = form.instance
        user.is_active = False
        user.save()

        activ_link = 'http://' + get_current_site(self.request).domain + reverse('alpha:activate', kwargs={
            'uidb64': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
            'token': account_activation_token.make_token(user)
        })
        message = render_to_string('alpha/acc_active_email.html', {
            'user': user,
            'activ_link':activ_link,
        })
        send_mail(
            settings.ALPHA['MAIL_SUBJECT'],
            message,
            settings.DEFAULT_FROM_EMAIL,
            [form.cleaned_data.get('email')],
            fail_silently=False,
        )
        messages.add_message(self.request, messages.INFO, _('We send you a active link. Please confirm.'))
        return super().form_valid(form)


class ActivateView(View):
    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs.get('uidb64')))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = False

        if user and account_activation_token.check_token(user, kwargs.get('token')):
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(request, messages.INFO, _('Welcome to Center. Your account is now activate.'))
            return redirect(settings.LOGIN_REDIRECT_URL)

        return redirect('/')
