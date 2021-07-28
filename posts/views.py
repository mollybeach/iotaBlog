
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
    p = User.objects.get(pk=rp['pk'])
    p.firstname=rp['firstname']
    p.lastname=rp['lastname']
    p.email=rp['email']
    p.service=rp['service']
    p.telephone=rp['telephone']
    p.appointmentdate=rp['appointmentdate']
    p.save()
    return get(request)

def contact(request):
    return render(request, 'contact.html', contact)

def about(request):
    return render(request, 'about.html', about)

def calendar(request):
    if request.method=="POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('service') and request.POST.get('appointmentdate'):
            saveobj = User()
            saveobj.firstname=request.POST.get('firstname')
            saveobj.lastname=request.POST.get('lastname')
            saveobj.email=request.POST.get('email')
            saveobj.service=request.POST.get('service')
            saveobj.telephone=request.POST.get('telephone')
            saveobj.appointmentdate=request.POST.get('appointmentdate')
            cursor=connection.cursor()
            cursor.execute("INSERT INTO User(firstname, lastname, email, service, telephone, appointmentdate) values(' "+saveobj.firstname+ "', ' "+saveobj.lastname+ "',  ' "+saveobj.email+ "', '" + saveobj.service+ "'" +", '"+saveobj.telephone+"', '"+saveobj.appointmentdate+"')")
            messages.success(request, "Thank you! "+saveobj.firstname+ " "+saveobj.lastname+ " has successfully scheduled appointment on "+ saveobj.appointmentdate+" for "+ saveobj.service+" ")
        return render(request, 'calendar.html')
    else:
        return render(request, 'calendar.html')










