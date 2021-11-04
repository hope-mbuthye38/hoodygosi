from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import estatedomin, News ,Business, Profile
# Create your views here.
def home(request):
    context={
        'estate domin': estatedomin.objects.all()
    }
    return render(request,'neighbourhood/home.html', context)

class EstatedominDetailView(LoginRequiredMixin, DetailView):
     model = estatedomin


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['image','bio','estatedomin']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

