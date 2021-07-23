
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
from .models import Post
from .models import employee, client
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts':posts})

def contact(request):
    return render(request, 'contact.html')
def posts(request):
    return render(request, 'posts.html')

def about(request):
    return render(request, 'about.html')

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




def calendar(request):
    if request.method=="POST":
        if request.POST.get('first_name') and request.POST.get('appointment_date'):
            saveobj = client()
            saveobj.first_name=request.POST.get('first_name')
            saveobj.appointment_date=request.POST.get('appointment_date')
            cursor=connection.cursor()
            cursor.execute("insert into client(first_name, appointment_date) values(' "+saveobj.first_name+ "', '" + saveobj.appointment_date+ "')")
            messages.success(request, "Client name  "+saveobj.first_name+ " has successfully scheduled appointment on "+ saveobj.appointment_date)
            return render(request, 'calendar.html')
    else:
        return render(request, 'calendar.html')





        
        #saveobj.empid=request.POST.get('empid')
        #saveobj.empphone=request.POST.get('empphone')
        #saveobj.empaddress=request.POST.get('empaddress')
        return redirect('/posts/')
def home(request, year, month):
    firstname = 'John'
    month = month.capitalize()

    #Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)

    #Get current year 
    now = datetime.now()
    current_year = now.year()

    #Get current time
    current_time = now.time()
    #year = now.strftime("%Y")
    #month = now.strftime("%m")
    #day = now.strftime("%d")
    #time = now.strftime("%H:%M:%S")




    return render(request, 
        'home.html', {
        'first_name':firstname,
        'year':year,
        'month':month,
        'month_number':month_number,
        'cal':cal,
        'current_year':current_year,
        #'time':time,
        'current_time':current_time,
    })
    # 'day':day