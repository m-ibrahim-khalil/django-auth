from django.contrib.auth.decorators import login_required
from django.shortcuts import render

app_name = "myapp"


def index(request):
    return render(request, "myapp/index.html")


@login_required
def profile(request):
    return render(request, "myapp/profile.html")


@login_required
def manage_account(request):
    return render(request, "myapp/manage_account.html")
