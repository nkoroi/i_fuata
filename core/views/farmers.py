from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import *
from ..models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import farmer_required


class FarmerCreationForm(CreateView):
    model = User
    form_class = FarmerCreationForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'farmer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('farmer:dashboard')

@method_decorator([login_required, student_required], name='dispatch')
