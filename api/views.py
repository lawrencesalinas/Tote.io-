from math import prod
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products
from .models import Product
from .serializers import ProductSerializer
# Create your views here.



@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    # print(request)
    product = None
    for i in products:
        # if product id matches pk
        if i['_id'] == pk:
            product = i
            break
    return Response(product)
