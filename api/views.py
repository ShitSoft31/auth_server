from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import MeSerializer


class MeView(APIView):
    def post(self, request):
        serializer = MeSerializer(request.user, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)
