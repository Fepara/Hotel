# hoteis/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário após registro
            messages.success(request, f"Conta criada com sucesso para {user.username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'hoteis/register.html', {'form': form})
