from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .forms import RegisterForm


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def register(request):
    next_url = request.GET.get("next") or request.POST.get("next", "")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            if next_url:
                return redirect(next_url)

            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
            "next": next_url,
        },
    )
