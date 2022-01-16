from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products
# Create your views here.


@api_view(['GET'])
def getProducts(request):
    return Response(products)

