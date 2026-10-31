from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from .forms import RegisterForm, SettingsForm


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return self._render_form(request, RegisterForm())

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect(self._get_next_url(request) or "login")

        return self._render_form(request, form)

    def _get_next_url(self, request):
        return request.GET.get("next") or request.POST.get("next", "")

    def _render_form(self, request, form):
        return render(
            request,
            "registration/register.html",
            {
                "form": form,
                "next": self._get_next_url(request),
            },
        )


@method_decorator(login_required, name="dispatch")
class SettingsView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self._render_form(request, SettingsForm(instance=request.user))

    def post(self, request):
        form = SettingsForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated!")

            return redirect("settings")

        return self._render_form(request, form)

    def _render_form(self, request, form):
        return render(
            request,
            "account/settings.html",
            {
                "form": form,
            },
        )
