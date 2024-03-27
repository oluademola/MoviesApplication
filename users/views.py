from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm
from django.views.decorators.http import require_POST

# Create your views here.
@require_POST
def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}.'.format(un))
            return redirect('sign_in')
            
    elif request.method == "GET":
        form = UserSignUpForm()
        
    return render(request, 'users/signup.html', {'form': form})