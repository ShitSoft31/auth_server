from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Configures the central user management application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
    verbose_name = "Accounts"
