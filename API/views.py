from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import Schems
from rest_framework.response import Response
from rest_framework import status ,mixins
from .models import AdminDetails
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.authentication import TokenAuthentication
# Create your views here.
#create admin view
class AdminView(APIView):
    def get_username(self,username):
        try:
            user = User.objects.get(username=username)
        except :
            return "Not Found"
        return user   
    # def post(self,request):
    #     serializer=AdminSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         #print(serializer.id)
    #         user=serializer.save()
    #         data=AdminDetails(fname=request.data['first_name'],lname=request.data['lname'],email=request.data['email'],mobile=request.data['mobile'],image=request.data['image'],
    #         usertype=request.data['usertype'],userid=user,status=request.data['status'])
    #         data.save()
    #         return Response({"massage":"Saved successfully","status":status.HTTP_200_OK})
    def post(self,request):
        user=self.get_username(self.request.data['username'])
        
        if user=='Not Found':
            serializer=SignUpSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user=serializer.save()
                #print(user.id)
                print(request.FILES['image'])
                extra_info=AdminDetails(user_id=user.id,mobile=request.data['mobile'],image=request.FILES['image'])
                extra_info.save()
                reponse={
                    "Status":status.HTTP_201_CREATED,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Admin added successfully",
                    "Data":{
                        "id":user.id,
                        "username":user.username,
                        "first_name":user.first_name,
                        "email":user.email,
                        
                    }
                }
                return Response(reponse)
        else:
            reponse={
                    "Status":status.HTTP_400_BAD_REQUEST,
                    "Error":{
                        "ErrorCode":400,
                        "ErrorMessage":"Username already register"
                    }
              }
            return Response(reponse)

#Admin login api view
class AdminLogin(APIView):
             
        
    def post(self,request,format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            reponse={
                    "Status":status.HTTP_400_BAD_REQUEST,
                    "Error":{
                        "ErrorCode":400,
                        "ErrorMessage":"Please provide both username and password"
                    }
              }
            return Response(reponse)
        else:                        
                        
            user = authenticate(username=username, password=password)
            if not user:
                reponse={
                    "Status":status.HTTP_404_NOT_FOUND,
                    "Error":{
                        "ErrorCode":404,
                        "ErrorMessage":"Invalid Credentials"
                    }
              }
                return Response(reponse)
            else:
                token, _ = Token.objects.get_or_create(user=user)
                reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Login successfully",
                    "Data":{
                        "id":user.id,
                        "first_name":user.first_name,
                        "username":user.username,
                        "token":token.key
                
                        
                    }
                }
                return Response(reponse)
        
    # def post(self,request):
    #     username=request.data['userid']
    #     password=request.data['password']
    #     admin=TblAdmin.objects.filter(userid=username,password=password)
    #     if admin:
    #         return Response({"massage":"Login Successfully"})
    #     else:
    #         return Response({"massage":"Credentials are not valid"})    
class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


#Scheme view
class SchemeView(APIView):        
    #queryset=Schems.objects.all()
    #serializer_class=SchemeSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes=(TokenAuthentication,)             # <-- And here
    permission_classes = (IsSuperUser,)
   

    def get(self,request,id=None):
        schemes=Schems.objects.all()
        serializer_data=SchemeSerializer(schemes,many=True)
        print(serializer_data.data)
        reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Schemes list",
                    "Data":{

                        "data":serializer_data.data
                        
                    }
                }
        return Response(reponse)

   
    def post(self,request):
        serializer=SchemeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            scheme=serializer.save()
            #print(user.id)
            reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Scheme saved successfully",
                    "Data":{

                        "id":scheme.id,
                        "scheme_name":scheme.scheme_name
                        
                    }
                }
            return Response(reponse)
    
    def delete(self,request):
        id=self.request.query_params.get('id')
        #print(id)
        Schems.objects.get(id=id).delete()
        reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Scheme deleted successfully",
                    "Data":{

                        "id":id
                        
                    }
                }
        return Response(reponse)

    
    def put(self, request, *args, **kwargs):
        #print("inside put")
        scheme=Schems.objects.get(id=self.request.query_params.get('id'))
        #print(scheme)
        serializer_data=SchemeSerializer(instance=scheme,data=request.data,partial=True)
        if serializer_data.is_valid(raise_exception=True):
            scheme=serializer_data.save()
            reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Scheme Updated successfully",
                    "Data":{

                        "id":scheme.id,
                        "scheme_name":scheme.scheme_name
                        
                    }
                }
            return Response(reponse)  
        # print("hih")
        # return self.partial_update(request, *args, **kwargs) 

#Scheme Category view
class SchemeCategoryView(generics.GenericAPIView, mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.ListModelMixin):        
    queryset=SCategory.objects.all()
    serializer_class=SchemeCategorySerializer
    permission_classes = (IsSuperUser,)
   
    def get(self,request,id=None):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
    def delete(self,request):
        id=self.request.query_params.get('id')
        #print(id)
        SCategory.objects.get(id=id).delete()
        return Response({"message":"Success"})

    
    def put(self, request, *args, **kwargs):
        print("inside put")
        category=SCategory.objects.get(id=self.request.query_params.get('id'))
        #print(scheme)
        serializer_data=SchemeCategorySerializer(instance=category,data=request.data,partial=True)
        if serializer_data.is_valid(raise_exception=True):
            serializer_data.save()
            return Response({"massage":"success"})  
        # print("hih")
        # return self.partial_update(request, *args, **kwargs) 



#all Scheme category get api
class GetAllSchemeCategoryView(APIView):
    def get(self,request):
        schemes_category=SCategory.objects.all()
        serializer_data=SchemeCategorySerializer(schemes_category,many=True)
        print(serializer_data.data)
        reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Scheme Category  list",
                    "Data":{

                        "data":serializer_data.data
                        
                    }
                }
        return Response(reponse)


#all centered Scheme  get api
class GetAllCenterSchemeView(APIView):
    def get(self,request):
        schemes=Schems.objects.filter(s_type=1)
        serializer_data=SchemeSerializer(schemes,many=True)
        print(serializer_data.data)
        reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Centered Scheme   list",
                    "Data":{

                        "data":serializer_data.data
                        
                    }
                }
        return Response(reponse)
        
#Get all centered Scheme based on category id  get api
class GetAllCenterSchemeBasedonCategoryView(APIView):
    def get(self,request):
        schemes=Schems.objects.filter(s_type=1,s_category=self.request.query_params.get('cat_id'))
        print("schemes",schemes)
        serializer_data=SchemeSerializer(schemes,many=True)
        print(serializer_data.data)
        reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"Category Based Centered Scheme   list",
                    "Data":{

                        "data":serializer_data.data
                        
                    }
                }
        return Response(reponse)


#Get all centered Scheme based on category id  get api
class GetAllSchemesBasedOnStateView(APIView):
    def get(self,request):
        schemes=Schems.objects.filter(s_state=self.request.query_params.get('s_id'))
        print("schemes",schemes)
        serializer_data=SchemeSerializer(schemes,many=True)
        print(serializer_data.data)
        reponse={
                    "Status":status.HTTP_200_OK,
                    "Error":{
                        "ErrorCode":0,
                        "ErrorMessage":"No Error"
                    },
                    "Message":"State level Scheme   list",
                    "Data":{

                        "data":serializer_data.data
                        
                    }
                }
        return Response(reponse)

# #Get Scheme with details based on scheme id view
# class GetSchemesWithDetailView(APIView):
#     def get(self,request):
#         schemes=Schems.objects.get(id=self.request.query_params.get('id'))
#         print("schemes",schemes)
#         serializer_data=SchemeWithDetailSerializer(schemes,partial=True)
#         print(serializer_data.data)
#         reponse={
#                     "Status":status.HTTP_200_OK,
#                     "Error":{
#                         "ErrorCode":0,
#                         "ErrorMessage":"No Error"
#                     },
#                     "Message":" Scheme with detail ",
#                     "Data":{

#                         "data":serializer_data.data
                        
#                     }
#                 }
#         return Response(reponse)


import datetime

x = datetime.datetime.now()


#Get state and centered Scheme based on userinfo
class GetSchemesBasedOnUserView(APIView):
    def post(self,request):
        age=request.data['age']
        age_range=x.year-int(age)
        serializer=CheckElegibilitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            schemes_for_center=Schems.objects.filter(s_type=1,scheme_for__icontains=request.data['gender'],
                marriage__icontains=request.data['marital'],scheme_age__icontains=age_range,family_income=request.data['income'],
                b_category=request.data['b_category'],occupation__icontains=request.data['occupation'])
            schemes_for_state=Schems.objects.filter(s_type=0,scheme_for__icontains=request.data['gender'],
                marriage__icontains=request.data['marital'],scheme_age__icontains=age_range,family_income=request.data['income'],
                b_category=request.data['b_category'],occupation__icontains=request.data['occupation'],s_state=request.data['state'])
        
            
            # print("state schemes")
            # for i in schemes_for_state:
            #     print(i.id)
            #     print(i.occupation)
            # # print("center schemes")
            # for i in schemes_for_center:
            #     print(i.id)
            #     #print(i.occupation)    
            serializer_data_for_center=SchemesForUserSerializer(schemes_for_center,many=True)
            serializer_data_for_state=SchemesForUserSerializer(schemes_for_state,many=True)
            
            print(serializer_data_for_center.data)
            reponse={
                
                "status":200,
                "message":"ok",
                "data": {
                    "statelist":serializer_data_for_state.data,
                    "centerallist":serializer_data_for_center.data
                }
            }


            return Response(reponse)

