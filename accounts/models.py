"""Models for the central User application."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Central ShitSoft account shared by every application in the ecosystem.

    Inherits Django's ``AbstractUser`` instead of using a separate profile
    table so the username-based login flow stays identical to Django's
    built-in implementation. ShitSoft-specific columns can be appended here;
    currently only ``bio`` is required.
    """

    bio = models.TextField(
        blank=True,
        default="",
        help_text="Short public description of the user.",
    )
