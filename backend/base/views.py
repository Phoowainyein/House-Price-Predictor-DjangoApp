from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .test_data import test_tt


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        'api/test'
    ]
    return Response(routes)


@api_view(['GET'])
def get_test_data(request):
    return JsonResponse(test_tt, safe=False)
