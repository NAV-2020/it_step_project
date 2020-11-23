from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.template.response import TemplateResponse
from django.views.generic import CreateView, View

from .forms import SignUpForm, UserSettingsForm


User = get_user_model()

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class UserSettingsView(View):
    template_name = 'users/settings.html'
    from_class = UserSettingsForm

    def get(self, request, *args, **kwargs):
        form = self.from_class()
        context = {
                'form':form
                }
        return TemplateResponse(request, 
                                template=self.template_name,
                                context=context)
    