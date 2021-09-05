from rest_framework.views import APIView
import re
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .helpers import *
from django.contrib.auth import authenticate , login

class LoginView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            #print("\nlogin")
            #print(data.get('password'))
            
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            if data.get('password') == '' :
                response['message'] = 'key password not found'
                raise Exception('key password empty')


            
            
            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user is None:
                response['message'] = 'invalid username , user not found'
                raise Exception('invalid username not found')
            """
            if not Profile.objects.filter(user = check_user).first().is_verified:
                response['message'] = 'your profile is not verified'
                raise Exception('profile not verified')
            """   
            
            user_obj = authenticate(username = data.get('username') , password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'

            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')
                
            
        except Exception as e :
            print(e)
            
        return Response(response)
            
                
    
    
LoginView = LoginView.as_view()




class RegisterView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            
            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user:
                response['message'] = 'username  already taken'
                raise Exception('username  already taken')
			
            if data.get('password') != data.get('password1'):
                response['message'] = 'Those passwords didn’t match. Try again'
                raise Exception('Those passwords didn’t match. Try again')

            if len(data.get('password')) < 8:
                response['message'] = 'Password must be 8 charecters long'
                raise Exception('Password must be 8 charecters long')

            if not re.search("[a-z]", data.get('password')):
                response['message'] = 'Password must contain at least one lowercase'
                raise Exception('Password must contain at least one lowercase')
    
            if not re.search("[A-Z]", data.get('password')):
                response['message'] = 'Password must contain at least one Uppercase'
                raise Exception('Password must contain at least one Uppercase')

            if not re.search("[0-9]", data.get('password')):
                response['message'] = 'Password must contain at least one number'
                raise Exception('Password must contain at least one number')

            if not re.search("[~!@#$%^&-+_*]", data.get('password')):
                response['message'] = 'Password must contain a leaste one charecter'
                raise Exception('Password must contain at least one charecter')


            #print("register ")
            #print(data.get('password'))
			
    
            
            user_obj = User.objects.create(email = data.get('username') , username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token = generate_random_string(20)
            Profile.objects.create(user = user_obj , token = token)
            
            response['message'] = 'User created '
            response['status'] = 200
            
                
            
        except Exception as e :
            print(e)
            
        return Response(response)
            
                
RegisterView = RegisterView.as_view()
        