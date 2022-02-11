from django.shortcuts import render
#import perssion classes
from rest_framework.decorators import api_view, permission_classes
# import for permissions level IsAuthenticated user must be authenticated to access view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.models import Product
from api.serializers import ProductSerializer
# error handlers
from rest_framework import status

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    # get by id 
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
       