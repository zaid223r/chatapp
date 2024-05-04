from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect

from .forms import CustomUserCreationForm


def main_page(request):
    return render(request,"main/mainpage.html")

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('mainpage')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

 