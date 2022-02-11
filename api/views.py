from math import prod
from django.shortcuts import render
#import perssion classes
from rest_framework.decorators import api_view, permission_classes
# import for permissions level IsAuthenticated user must be authenticated to access view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# from .products import products
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # print(data)
        print(self.user)
        serializer = UserSerializerWithToken(self.user).data
        # print(serializer)
        # for each key and values, loop through the items inside the serilizers
  
        # k are the keys, for each keys we plug in the v's
        # adding it to the dictionary with a for loop
        for k, v in serializer.items():
            # print('this is k',k)
            # print('VVVV',v)
        # output the initial response when we get our first token
            data[k] = v
        
        return data
class MyTokenObtainPairView(TokenObtainPairView):
    # serializer class that returns user data
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

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
       
     
    

