from rest_framework import serializers
from django.contrib.auth import get_user_model


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "bio",
            "date_joined",
            "last_login",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        scopes = self.context["request"].auth.scope.split()

        if "read:firstname" not in scopes:
            self.fields.pop("first_name")

        if "read:lastname" not in scopes:
            self.fields.pop("last_name")

        if "read:username" not in scopes:
            self.fields.pop("username")

        if "read:email" not in scopes:
            self.fields.pop("email")

        if "read:bio" not in scopes:
            self.fields.pop("bio")

        if "read:date_joined" not in scopes:
            self.fields.pop("date_joined")

        if "read:last_login" not in scopes:
            self.fields.pop("last_login")
