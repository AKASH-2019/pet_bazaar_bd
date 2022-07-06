from django.shortcuts import render
from api import database

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
import json

# Create your views here.


@api_view(['GET'])
@parser_classes([JSONParser])
def productPagination(request,payload):
    # payload = json.dumps({})
    print(payload)
    data = database.db('pet.test_product__pagination',payload)
    print("data")
    print(data)
    return Response(data)

