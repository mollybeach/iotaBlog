
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

@csrf_exempt
def get(request):
    context= serializers.serialize('json', User.objects.all())
    return JsonResponse(context, safe=False)

@csrf_exempt
def post_product(request):
    if request.method == 'POST':
        rp = json.loads(request.body.decode('utf-8'))
        user = User(firstname=rp['firstname'],lastname=rp['lastname'],email=rp['email'],service=rp['service'],telephone=rp['telephone'],appointmentdate=rp['appointmentdate'])
        user.save()
        context = serializers.serialize('json', User.objects.all())
        return JsonResponse(context, safe=False)
    

@csrf_exempt
def delete_product(request):
    rp=json.loads(request.body.decode('utf-8'))
    User.objects.get(pk=rp['pk']).delete()
    return get(request)

@csrf_exempt
def update_product(request):
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

def calendar(request):
    if request.method=="POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('service') and request.POST.get('appointmentdate'):
            field = User()
            field.firstname=request.POST.get('firstname')
            field.lastname=request.POST.get('lastname')
            field.email=request.POST.get('email')
            field.service=request.POST.get('service')
            field.telephone=request.POST.get('telephone')
            field.appointmentdate=request.POST.get('appointmentdate')
            cursor=connection.cursor()
            cursor.execute("INSERT INTO User (firstname, lastname, email, service, telephone, appointmentdate) values(' "+field.firstname+ "', ' "+field.lastname+ "',  ' "+field.email+ "', '" + field.service+ "'" +", '"+field.telephone+"', '"+field.appointmentdate+"')")
            messages.success(request, "Thank you! "+field.firstname+ " "+field.lastname+ " has successfully scheduled appointment on "+ field.appointmentdate+" for "+ field.service+" ")
        return render(request, 'calendar.html')
    else:
        return render(request, 'calendar.html')










