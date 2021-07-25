from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

from app_test.models.CharacterKihon import CharacterKihon
from app_test.forms import CharacterForm

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html" 
    success_url = reverse_lazy('app_test:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user 
        return HttpResponseRedirect(self.get_success_url())

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'app_test/index.html')

def new(request):
    return render(request, 'app_test/new.html')

def add(request):
    characterkihon = CharacterKihon()
    form = CharacterForm(request.POST, instance=characterkihon)
    if form.is_valid():
        characterkihon = form.save(commit=False)
        characterkihon.save()
        return redirect('app_test:index')
    return render(request, 'app_test/add.html')
