from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("url-builder/", views.UrlBuilderView.as_view(), name="url-builder"),
]
