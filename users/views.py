from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import RegisterForm, AuthForm

def register_succes(request):
    context = {}
    return render(request, "register_succes.html", context)

def register(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            account = authenticate(username=username, password=password1)
            login(request, account)
            return redirect('register_succes')
        else:
            context["registration_form"] = form
    else:
        form = RegisterForm()
        context['register_form'] = form
    return render(request, "register.html", context)

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("homepage")

    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("homepage")

    else:
        form = AuthForm()

    context["login"] = form
    return render(request, "login.html", context)

def logout(request):
    logout(request)
    return redirect('/')   
