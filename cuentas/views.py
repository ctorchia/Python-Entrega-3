from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from cuentas.forms import *

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def register(request):
    if request.method == "POST":
        form = PerfilCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("perfil_detail")
    else:
        form = PerfilCreateForm()
    return render(request, "cuentas/register.html", {"form": form})


@login_required
def profile_detail(request):
    return render(request, "cuentas/perfil_detail.html", {"user": request.user})


@login_required
def profile_change(request):
    if request.method == "POST":
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil_detail")
    else:
        form = PerfilChangeForm(instance=request.user)
    
    return render(request, "cuentas/perfil_change.html", {"form": form})

    
@login_required
def password(request):

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()

            update_session_auth_hash(request, user)

            return redirect("perfil_detail")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "cuentas/password.html", {"form": form})