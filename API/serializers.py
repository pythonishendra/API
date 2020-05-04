from django.contrib.auth import get_user_model
UserModel = get_user_model()
from rest_framework import serializers
from .models import *


from django.contrib.auth import get_user_model


UserModel = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        
        user = UserModel.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user

    class Meta:
        model = UserModel
        fields = ( 'id','password','is_staff','username','first_name','email','is_active' )

#Members list serializer
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAdmin
        fields='__all__'

#Scheme serializer
class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schems
        fields='__all__'        


#Scheme serializer
class SchemeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SCategory
        fields='__all__'        
                
#Scheme detail serializer
class SchemeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=SchemesDetails
        fields='__all__'                

#Scheme listwith Detail serializer
# class SchemeWithDetailSerializer(serializers.ModelSerializer):
#     detail=SchemeDetailSerializer(read_only=True)
#     class Meta:
#         model=Schems
#         fields=('id','detail')

#Scheme serializer
class SchemesForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schems
        fields='__all__'       

#check eligibility  serializer
class CheckElegibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Eligibilitycheckedmember
        fields='__all__'       
