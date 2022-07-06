from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from urllib.parse import urlencode

from datetime import datetime
from django.conf import settings
from django.contrib import messages
# from app.models import User
import requests


from pet import database
import json

# Create your views here.

def privacy(request):
    return render(request, 'authentication/signup.html')


def signup(request):
    return render(request, 'authentication/signup.html')

@api_view(['POST'])
@csrf_protect
def signupUpsert(request):
    if request.method == "POST":
        storeProcedure = 'pet.user__upsert'
        user_id = 0 
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        # confirmaPassword = request.POST['confirmPassword']
       
        payload = json.dumps({"user_id":user_id,"email":email,"username":username,"password":password})
        data = database.db(storeProcedure,payload)

        return JsonResponse(data, safe=False)



def login(request):
    return render(request, 'authentication/login.html')

def social_login(request, slug):
    way = slug

    if(slug == "facebook"):
        return redirect('/petbazaar/facebook-login')
    if(slug == "google"):
        return redirect('/petbazaar/google-login')



@api_view(['POST'])
@csrf_protect
def loginUpsert(request):

    if request.method == "POST":
        storeProcedure = 'pet.user__login'
        email = request.POST['email']
        password = request.POST['password']
        payload = json.dumps({"email":email,"password":password})

        data = database.db(storeProcedure,payload)

        if(data[0]['auth_status']):
            request.session['user_record'] = json.dumps(data[0]['ret_data'])
            return JsonResponse(data, safe=False)
    


def logout(request):
    try:
        del request.session['user_record']
    except KeyError:
        pass
    # return render(request, 'authentication/login.html')
    return redirect('/')



def google_login(request):
    redirect_uri = "%s://%s%s" % (
        # request.scheme, request.get_host(), reverse('pain:google_login')
        request.scheme, request.get_host(), reverse('authentication:google_login')
    )
    if('code' in request.GET):
        params = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'redirect_uri': redirect_uri,
            'client_id': settings.GP_CLIENT_ID,
            'client_secret': settings.GP_CLIENT_SECRET
        }

        url = 'https://accounts.google.com/o/oauth2/token'
        response = requests.post(url, data=params)
        url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        access_token = response.json().get('access_token')
        response = requests.get(url, params={'access_token': access_token})
        # response = request.GET(url, params={'access_token': access_token})
        user_data = response.json()
        email = user_data.get('email')
        if email:
            # code goes here ................
            # user, _ = User.objects.get_or_create(email=email, username=email)

            gender = user_data.get('gender', '').lower()
            if gender == 'male':
                gender = 'M'
            elif gender == 'female':
                gender = 'F'
            else:
                gender = 'O'
            data = {
                'first_name': user_data.get('name', '').split()[0],
                'last_name': user_data.get('family_name'),
                'logo_image': user_data.get('picture'),
                'gender': gender,
                'email':email,
                'active': True
            }
            # print(data)
            storeProcedure = 'pet.social_user__upsert'
            payload = json.dumps(data)
            data = database.db(storeProcedure,payload)
            if(data[0]['ret_val'] > 0 and data[0]['user_id'] > 0 and data[0]['ret_val'] == data[0]['user_id']):
                request.session['user_record'] = json.dumps(data[0]['ret_data'])
                # return JsonResponse(data, safe=False)
                return redirect('/checkout')

        else:
            messages.error(
                request,
                'Unable to login with Gmail Please try again'
            )
        return redirect('/')
    else:
        url = "https://accounts.google.com/o/oauth2/auth?client_id=%s&response_type=code&scope=%s&redirect_uri=%s&state=google"
        scope = [
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email"
        ]
        scope = " ".join(scope)
        url = url % (settings.GP_CLIENT_ID, scope, redirect_uri)
        return redirect(url)


def facebook_login(request):
    redirect_uri = "%s://%s%s" % (
        request.scheme, request.get_host(), reverse('authentication:facebook_login')
    )
    if('code' in request.GET):
        code = request.GET.get('code')
        url = 'https://graph.facebook.com/v2.10/oauth/access_token'
        params = {
            'client_id': settings.FB_APP_ID,
            'client_secret': settings.FB_APP_SECRET,
            'code': code,
            'redirect_uri': redirect_uri,
        }
        response = requests.get(url, params=params)
        params = response.json()
        params.update({
            'fields': 'id,last_name,first_name,picture,birthday,email,gender'
        })
        url = 'https://graph.facebook.com/me'
        user_data = requests.get(url, params=params).json()
        email = user_data.get('email')
        if email:
            # user, _ = User.objects.get_or_create(email=email, username=email)
            gender = user_data.get('gender', '').lower()
            dob = user_data.get('birthday')
            if gender == 'male':
                gender = 'M'
            elif gender == 'female':
                gender = 'F'
            else:
                gender = 'O'
            data = {
                'first_name': user_data.get('first_name'),
                'last_name': user_data.get('last_name'),
                'email':email,
                'logo_image': user_data.get('picture', {}).get('data', {}).get('url'),
                'gender': gender,
                # 'dob': datetime.strptime(dob, "%m/%d/%Y") if dob else None,
                'active': True
            }
            # user.__dict__.update(data)
            # user.save()
            # user.backend = settings.AUTHENTICATION_BACKENDS[0]
            # login(request, user)
            storeProcedure = 'pet.social_user__upsert'
            payload = json.dumps(data)
            data = database.db(storeProcedure,payload)
            if(data[0]['ret_val'] > 0 and data[0]['user_id'] > 0 and data[0]['ret_val'] == data[0]['user_id']):
                request.session['user_record'] = json.dumps(data[0]['ret_data'])
                # return JsonResponse(data, safe=False)
                return redirect('/checkout')
        else:
            messages.error(
                request,
                'Unable to login with Facebook Please try again'
            )
        return redirect('/')
    else:
        url = "https://graph.facebook.com/oauth/authorize"
        params = {
            'client_id': settings.FB_APP_ID,
            'redirect_uri': redirect_uri,
            'scope': 'email,public_profile,user_birthday'
        }
        url += '?' + urlencode(params)
        return redirect(url)