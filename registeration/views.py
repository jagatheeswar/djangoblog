from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserupForm, UserMyForm, ProfileUpdateForm, UserupForm, Userupdateform, Phonenumbers, Phone, Birthday
from .models import Userdetails


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registeration/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserupForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        u_formtwo = Userupdateform(request.POST, instance=request.user.userdetails)                           
        p_honeform = Phone(request.POST, instance=request.user.phonenumbers)
        B_form = Birthday(request.POST, instance=request.user.phonenumbers)
        if u_form.is_valid() and p_form.is_valid() and u_formtwo.is_valid() and B_form.is_valid():
            u_form.save()
            p_form.save()
            u_formtwo.save()
            B_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserupForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        B_form = Phone(instance=request.user.phonenumbers)
        u_formtwo = Userupdateform(instance=request.user.userdetails)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'u_formtwo': u_formtwo,
        'B_form': B_form
    }

    return render(request, 'registeration/profile.html', context)
