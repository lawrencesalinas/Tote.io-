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
# import make_password to hash password
from django.contrib.auth.hashers import make_password
# error handlers
from rest_framework import status
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

# create a user
@api_view(['POST'])  
def registerUser(request):
    data = request.data
    # create a user with create method
    user = User.objects.create(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        # make_password was used to hash pashword from request
        password=make_password(data['password'])
    )
    
    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
# added permission class IsAuthenticated so only users can see their profile
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# route only for admin to see, use IsAdmin for admins to see
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
       
     
    

