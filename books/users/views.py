from django.shortcuts import render, redirect
from .forms import UserAdminCreatingForm
from django.contrib.auth.decorators import login_required


@login_required
def register(request):
    form = UserAdminCreatingForm()
    if request.method == 'POST':
        form = UserAdminCreatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(request, 'register.html', {'form': form})