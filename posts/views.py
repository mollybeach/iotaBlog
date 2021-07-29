
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import User
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import calendar
from django.template import loader
from django.template import RequestContext, loader
from calendar import HTMLCalendar
from datetime import datetime
from posts import models
import json
from django.core import serializers


def index(request):
    return render(request, 'users/index.html')
appname = 'Users'

def posts(request):
    return render(request, "posts.html")

def calendar(request):
    return render(request, 'calendar.html')
    
@csrf_exempt
def get(request):
    context= serializers.serialize('json', User.objects.all())
    return JsonResponse(context, safe=False)

@csrf_exempt
def post_user(request):
    if request.method == 'POST':
        rp = json.loads(request.body.decode('utf-8'))
        user = User(firstname=rp['firstname'],lastname=rp['lastname'],email=rp['email'],service=rp['service'],telephone=rp['telephone'],appointmentdate=rp['appointmentdate'])
        user.save()
        context = serializers.serialize('json', User.objects.all())
        return JsonResponse(context, safe=False)
    

@csrf_exempt
def delete_user(request):
    rp=json.loads(request.body.decode('utf-8'))
    User.objects.get(pk=rp['pk']).delete()
    return get(request)

@csrf_exempt
def update_user(request):
    rp=json.loads(request.body.decode('utf-8'))
    field = User.objects.get(pk=rp['pk'])
    field.firstname=rp['firstname']
    field.lastname=rp['lastname']
    field.email=rp['email']
    field.service=rp['service']
    field.telephone=rp['telephone']
    field.appointmentdate=rp['appointmentdate']
    field.save()
    return get(request)

def contact(request):
    return render(request, 'contact.html', contact)

def about(request):
    return render(request, 'about.html', about)











