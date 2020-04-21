from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from class_system.classes.models import Assisted


def register(request):
    context = {'company': settings.NAME_COMPANY}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    defaults = {
        'extra_context': context,
        'form': form,
    }
    return render(request, 'register.html', defaults)


@login_required
def dashboard(request):
    assisted = Assisted.objects.filter(user=request.user)
    context = {'company': settings.NAME_COMPANY, 'assisted': assisted}
    return render(request, 'dashboard.html', context)
