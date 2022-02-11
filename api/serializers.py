from rest_framework import serializers
from django.contrib.auth.models import User
# import refresh token
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id', 'username', 'email', 'name', 'isAdmin']
        
        # created a method, self is serializer, obj is the user obj
        # get_ is from django
    def get_name(self, obj):
        # to use name, we need to let UserSerializer on top to know about it
        # pass first_name paramaeter to name
        name = obj.first_name
        # if user doesn't submit a name return an email.
        if name == '':
            name = obj.email
        return name
    
    def get__id(self, obj):
        return obj.id
    
    def get_isAdmin(self, obj):
        return obj.is_staff
    
# create new serializer with token
# extend user serializer to have all the serizaliers plus token
class UserSerializerWithToken(UserSerializer):
    # serializer method 
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id', 'username', 'email', 'name', 'isAdmin', 'token']
        
    def get_token(self, obj):
        # as we're generating or serializnng a user 
        # we're gonna take that user object and we're gonna return back another token 
        # with the initial response
        token = RefreshToken.for_user(obj)
        # token needs to be a string value
        return str(token.access_token)
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
