from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

@api_view(["POST"])
def weight(height_data):
    try:
        body_height = json.loads(height_data.body)
        body_weight = str(body_height * 10)
        return JsonResponse('Body weight = ' + body_weight + " kg", safe=False)
    except ValueError as ve:
        return Response(ve.args[0], status.HTTP_404_BAD_REQUEST)

