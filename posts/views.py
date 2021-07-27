
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post
from .models import employee, client, Users
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from posts import models
#from django.views import View


from django.core import serializers

# Create your views here.

def index(request):
    index = Post.objects.all()
    return render(request, 'index.html', {'index':index})

def contact(request):
    contact = {'user': request.user}
    return render(request, 'contact.html', contact)

#write a function to get all the data from the the client table




   # cursor=connection.cursor()
   # cursor.execute("select * from client")
   # posts = cursor.fetchall()
    #return render(request, 'posts.html', {'posts': posts})
#and render the data to posts.html
'''
def posts(request):
    cursor=connection.cursor()
    cursor.execute("select * from client")
    data = cursor.fetchall()
    dataj = JsonResponse({"data": data})
    return render(request, 'posts.html', {dataj:dataj})


class DataView(View):  
        def get(self, request, *args, **kwargs):
            if request.is_ajax():
                tasks = client.objects.all()
                task_serializers = serializers.serialize('json', tasks)
                return JsonResponse(task_serializers, safe=False)


def dataview (self, request, *args, **kwargs):
            if request.is_ajax():
                tasks = client.objects.all()
                task_serializers = serializers.serialize('json', tasks)
                return JsonResponse(task_serializers, safe=False)
            return JsonResponse({"message": 'wrong validation'})   
            return JsonResponse({"message": 'wrong validation'})   
'''
def about(request):
    about = {'user': request.user}
    return render(request, 'about.html', about)

def calendar(request):
    if request.method=="POST":
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('service') and request.POST.get('appointment_date'):
            saveobj = client()
            saveobj.first_name=request.POST.get('first_name')
            saveobj.last_name=request.POST.get('last_name')
            saveobj.email=request.POST.get('email')
            saveobj.service=request.POST.get('service')
            saveobj.telephone=request.POST.get('telephone')
            saveobj.appointment_date=request.POST.get('appointment_date')
            cursor=connection.cursor()
            cursor.execute("INSERT INTO client(first_name, last_name, email, service, telephone, appointment_date) values(' "+saveobj.first_name+ "', ' "+saveobj.last_name+ "',  ' "+saveobj.email+ "', '" + saveobj.service+ "'" +", '"+saveobj.telephone+"', '"+saveobj.appointment_date+"')")
            messages.success(request, "Thank you! "+saveobj.first_name+ " "+saveobj.last_name+ " has successfully scheduled appointment on "+ saveobj.appointment_date+" for "+ saveobj.service+" ")
        return render(request, 'calendar.html')
    else:
        return render(request, 'calendar.html')
#define a schedule function that gets data from the database from the client modal
#and sends it to a javascript script in calendar.html
#get data jsonresponse
#send the data to the javascript
#return the data to the calendar.html


def posts(request):
   # Users = Users.objects.all()
    return render(request, "posts.html")

def Users(request):
    queryset=models.Users.objects.all()
    print(queryset)
    return JsonResponse({"Users" : list(queryset.values())})
'''
def getdata(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM client")
    data = cursor.fetchall()
    return JsonResponse(data, safe=False)
'''


def insertrec(request):
    if request.method=="POST":
        if request.POST.get('empname') and request.POST.get('empjoindate'):
            saveobj = employee()
            saveobj.empname=request.POST.get('empname')
            saveobj.empjoindate=request.POST.get('empjoindate')
            cursor=connection.cursor()
            cursor.execute("insert into empjoin (empname, empjoindate) values(' "+saveobj.empname+ "', '" + saveobj.empjoindate+ "')")
            messages.success(request, "Employee name  "+saveobj.empname+ " Is save scucessfully")
            return render(request, 'insertrec.html')
    else:
        return render(request, 'insertrec.html')






