from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth

def index(request):
    return render(request , 'users/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request , user)
            return redirect('index')
    else:
        form = UserCreationForm()

    content =  {'form':form}
    return render(request, 'registration/register.html', content)

class logout(LoginRequiredMixin , View):
    def get(self,request,*args,**kwargs):
        auth.logout(request)
        return redirect("accounts:signup_page")
