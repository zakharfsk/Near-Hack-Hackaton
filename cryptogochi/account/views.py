from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm
'''
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit = False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
'''
def user_login(request):
    form = LoginForm(request.POST)
    user_form = UserRegistrationForm(request.POST)
    
    if request.method == 'post':    
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['log_user'], password = cd['log_pass'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit = False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['reg_pass'])
            # Save the User object
            new_user.save()
            return render(request, 'account/base.html', {'new_user': new_user})
    elif request.method == 'POST' and form.is_valid():
        form = LoginForm()
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form, 'user_form': user_form})