from django.shortcuts import render

app_name = "myapp"


def index(request):
    return render(request, "myapp/index.html")


def profile(request):
    return render(request, "myapp/profile.html")


def manage_account(request):
    return render(request, "myapp/manage_account.html")
