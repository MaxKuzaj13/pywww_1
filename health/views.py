from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .models import Health
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import HealthForm
from .permissions import BelongsToGroup
# Create your views here.


class ListHealthView(LoginRequiredMixin, ListView):
    model = Health
    template_name = 'health/list_health_view.html'
    context_object_name = 'health_list'

    def get_queryset(self):
        """
           A base view for displaying a list of objects from current logged user except Admin.
        """
        user = self.request.user
        group = BelongsToGroup.list_group(self, user)
        if "Admin" in group:
            return self.model.objects.filter()
        return self.model.objects.filter(user=self.request.user)


class CreateHealthView(LoginRequiredMixin, CreateView):
    model = Health
    form_class = HealthForm
    template_name = 'health/add_health.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('health:health_add')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     systolic_blood_pressure = cleaned_data.get("systolic_blood_pressure")
    #     diastolic_blood_pressure = cleaned_data.get("diastolic_blood_pressure")
    #     pulse = cleaned_data.get("pulse")
    #     glucoses = cleaned_data.get("glucoses")
    #
    #     if cc_myself and subject and "help" not in subject:
    #         msg = "Must put 'help' in subject when cc'ing yourself."
    #         self.add_error('cc_myself', msg)
    #         self.add_error('subject', msg)