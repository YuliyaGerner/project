from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('signin.html')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password1 = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                new_user = User.objects.create_user(username=username, email=email, password1=password1,
                                                    password2=password2)
                new_user.save()
                messages.success(request, 'Account was created for ' + user)
                login(request=request, user=new_user)

                return redirect('signin')

        context = {'form': form}
        return render(request, 'registration/signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('signup.html')
            else:
                messages.error(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/signin.html', context)


def logoutUser(request):
    if request.method == "POST":
        logout(request)

    return redirect('signin')
